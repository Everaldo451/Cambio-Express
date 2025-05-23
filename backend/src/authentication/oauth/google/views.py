from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpRequest
from django.urls import reverse
from django.shortcuts import redirect

from users.models import User

from .serializers import GoogleOAuthSerializer

from authentication.services import register_common_user
from authentication.services import JWTService
from authentication.services import generate_oauth_config, check_granted_scopes

from googleapiclient.discovery import build
import google_auth_oauthlib.flow

import logging

@api_view(["GET"])
def google_auth_redirect(request:HttpRequest|Request):	
	redirect_uri = f"http://{request.get_host()}{reverse('oauth2callback')}"
	logging.debug(f"Redirect uri: {redirect_uri}")
	flow = google_auth_oauthlib.flow.Flow.from_client_config(**generate_oauth_config(request, redirect_uri))
	flow.redirect_uri = redirect_uri
	authorization_url, state = flow.authorization_url(access_type = 'offline',prompt="consent")
	request.session['state'] = state
	request.session.save()

	if authorization_url:
		logging.debug(f"Authorization url: {authorization_url}")
		return redirect(authorization_url)
	
	return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GoogleOauthCallback(APIView):

	jwt_service = JWTService()

	def fetch_oauth_token(self, request:HttpRequest|Request, flow: google_auth_oauthlib.flow.Flow):
		authorization_response = request.build_absolute_uri()
		flow.fetch_token(authorization_response=authorization_response)
	
	
	def response_for_exist_user(self, request:HttpRequest|Request, user:User):
		if user.authentication_type!="oauth":
			return redirect("http://localhost:3000/oauth/fail?e='You must authenticate with your password.'")
		return self.jwt_service.generate_response(request, user, status.HTTP_201_CREATED)
	

	def response_for_non_exist_user(self, request:HttpRequest|Request, user_data:dict):
		register_data = register_common_user(request, {**user_data})
		if register_data["error"] == True:
			logging.debug(f"Response with error: {register_data["message"]}")
			return redirect(f"http://localhost:3000/oauth/fail?e='{register_data["message"]}'")
		
		logging.debug(f"Response with status 201. User registed sucessful.")
		user = register_data["obj"]
		return self.jwt_service.generate_response(request, user, status.HTTP_201_CREATED)
	

	def post(self, request:HttpRequest|Request, format=None):
		serializer = GoogleOAuthSerializer(data=request.data)
		if not serializer.is_valid():
			return redirect("http://localhost:3000/oauth/fail")
	
		state = request.session.get('state')
		if state is None: 
			return redirect("http://localhost:3000/oauth/fail?e='You don't accessed the oauth url.'")

		redirect_uri = f"http://{request.get_host()}{reverse('oauth2callback')}"
		flow = google_auth_oauthlib.flow.Flow.from_client_config(
			**generate_oauth_config(request, redirect_uri), 
			state=state
		)
		flow.redirect_uri = redirect_uri
		self.fetch_oauth_token(request, flow)

		credentials = flow.credentials
		features = check_granted_scopes(credentials)
		service = build('oauth2', "v2", credentials=credentials)

		if 'email' in features:
			userinfo = service.userinfo().get().execute()
			email = userinfo["email"]

			fetched_user = User.objects.filter(email=email).first()
			if fetched_user is not None and fetched_user.is_active:
				return self.response_for_exist_user(request, fetched_user)
			
			user_data = {
					"email": email, 
					"authentication_type": "oauth"
				}
			return self.response_for_non_exist_user(request, user_data)
		return Response({"message":"You didn't accepted the escopes."}, status=status.HTTP_400_BAD_REQUEST)

