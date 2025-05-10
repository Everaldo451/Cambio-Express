from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

from api.models import User

from .serializers import LoginSerializer, OAuthSerializer

from .extras.generate_jwt_response import generate_full_jwt_response
from .extras.register_user import register_user
from .extras.generate_oauth_config import generate_oauth_config
from .extras.oauth_utils import check_granted_scopes

from googleapiclient.discovery import build
import google_auth_oauthlib.flow

import logging

@api_view(["GET"])
def oauth_client_url(request:HttpRequest|Request):	
	redirect_uri = f"http://{request.get_host()}{reverse('oauth2callback')}"
	logging.debug(f"Redirect uri: {redirect_uri}")
	flow = google_auth_oauthlib.flow.Flow.from_client_config(**generate_oauth_config(request, redirect_uri))
	flow.redirect_uri = redirect_uri
	authorization_url, state = flow.authorization_url(access_type = 'offline',prompt="consent")
	request.session['state'] = state
	request.session.save()

	if authorization_url:
		logging.debug(f"Authorization url: {authorization_url}")
		return Response(
			{"message":"Authorization url generated successful.","authorization_url":authorization_url},
			status=status.HTTP_200_OK
		)
	
	return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def oauth_callback(request:HttpRequest|Request):
	serializer = OAuthSerializer(request.data)
	if not serializer.is_valid():
		return redirect("http://localhost:3000/oauth/fail")
	
	redirect_uri = f"http://{request.get_host()}{reverse('oauth2callback')}"
	state = request.session.get('state')
	if state is None: 
		return redirect("http://localhost:3000/oauth/fail?e='You don't accessed the oauth url.'")

	flow = google_auth_oauthlib.flow.Flow.from_client_config(**generate_oauth_config(request, redirect_uri), state=state)
	flow.redirect_uri = redirect_uri
	authorization_response = request.build_absolute_uri()
	flow.fetch_token(authorization_response=authorization_response)

	credentials = flow.credentials
	features = check_granted_scopes(credentials)
	service = build('oauth2', "v2", credentials=credentials)

	if 'email' in features:
		userinfo = service.userinfo().get().execute()
		email = userinfo["email"]

		user = User.objects.filter(email=email).first()
		if user.is_active:
			if user.authentication_type!="oauth":
				return redirect("http://localhost:3000/oauth/fail?e='You must authenticate with your password.'")
			return generate_full_jwt_response(request, user)
		
		register_data = register_user(request, {"email": email, "authentication_type": "oauth"})
		if register_data["error"] == True:
			stat = register_data["status"]
			error = register_data["content"]
			logging.debug(f"Response with status {stat}. Error: {error}")
			return redirect(f"http://localhost:3000/oauth/fail?e='{error}'")
		
		logging.debug(f"Response with status 200. User registed sucessful.")
		return generate_full_jwt_response(request, register_data["content"])

	return Response({"message":"You didn't accepted the escopes."}, status=status.HTTP_400_BAD_REQUEST)

	
@api_view(["POST"])
@csrf_protect
def password_login(request:HttpRequest|Request):

	logging.debug("Starting password login route.")
	serializer = LoginSerializer(data=request.data)
	if not serializer.is_valid():
		logging.debug(f"Response status 400. Invalid credentials. Errors: {serializer.errors}")
		return Response({"message":"Invalid credentials", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)	

	logging.debug("Verifying if user exists.")
	user = authenticate(**serializer.validated_data)
	if user is None:
		logging.debug(f"Response status 404. User not founded.")
		return Response({"message":"User don't exists"}, status=status.HTTP_404_NOT_FOUND)
	elif not user.is_active:
		logging.debug(f"Response status 403. Forbidden")
		return Response({"message":"The user isn't active"}, status=status.HTTP_403_FORBIDDEN)

	logging.debug("Response status 200. User logged successful.")
	return generate_full_jwt_response(request, user, status.HTTP_200_OK)	


@api_view(["GET"])
def logout(request:HttpRequest):

	response = redirect("http://localhost:3000")
	response.delete_cookie("refresh_token")
	return response
