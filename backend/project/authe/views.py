from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

from api.models import Company

from .form import LoginForm, UserRegisterExtras, CompanyRegisterExtras, RegisterForm, OAuthForm
from .serializers import UserSerializer

from .extras.generate_jwt_response import generate_full_jwt_response, generate_jwt_response_instance
from .extras.register_company import register_company
from .extras.register_user import register_user
from .extras.verify_exists_model import verify_exists_model
from .extras.generate_oauth_config import generate_oauth_config

import google.oauth2.credentials
import google_auth_oauthlib.flow

import logging
from dotenv import load_dotenv

load_dotenv()


@api_view(["GET"])
def get_jwt(request:HttpRequest):

	logging.debug(f"Get jwt string.")
	token_string = request.COOKIES.get("refresh_token")
	if token_string is not None:
		try:
			refresh_token = RefreshToken(token_string)
			logging.debug(f"Generating tokens.")
			return generate_jwt_response_instance(refresh_token)
		except TokenError as err: 
			logging.debug(f"Response status 400. Error: {err.args}")
			return Response({"message":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
		
	logging.debug("Response status 400. Token not provided")
	return Response({"message":"Token not provided"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request:HttpRequest):
	
	logging.debug("Getting the user data")
	serializer = UserSerializer(request.user)
	if not serializer.is_valid():
		logging.debug("Response status 500. Invalid serializer.")
		return Response({"message":"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	
	data = serializer.data
	data.pop("id")
	if not request.user.groups.filter(name="Company").exists():
		logging.debug("User isn't a company.")
		print("notCompany")
		data.pop("company")

	logging.debug(f"Response status 200. User data: {data}")
	return Response({"data":data})

@api_view(["GET"])
def oauth_client_url(request:HttpRequest):

	redirect_uri = reverse('oauth2callback')
	flow = google_auth_oauthlib.flow.Flow.from_client_config(**generate_oauth_config(request))
	flow.redirect_uri = redirect_uri
	authorization_url, state = flow.authorization_url(access_type = 'offline',prompt="consent")
	request.session['state'] = state

	if authorization_url:
		return Response({"url":authorization_url})
	
	return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def oauth_callback(request:HttpRequest):

	oauth_form = OAuthForm(request.GET)

	if not oauth_form.is_valid():
		return Response({"message":"OAuth response is invalid"}, status=status.HTTP_400_BAD_REQUEST)
	
	redirect_uri = reverse('oauth2callback')
	state = request.session.get('state')
	if state is None: 
		return

	flow = google_auth_oauthlib.flow.Flow.from_client_config(**generate_oauth_config(request), state=state)
	flow.redirect_uri = redirect_uri
	authorization_response = request.build_absolute_uri()
	flow.fetch_token(authorization_response=authorization_response)
	credentials = flow.credentials

	request.session["credentials"] = {
		'token': credentials.token,
		'refresh_token': credentials.refresh_token,
		'token_uri': credentials.token_uri,
		'client_id': credentials.client_id,
		'client_secret': credentials.client_secret,
		'granted_scopes': credentials.granted_scopes
	}

	
@api_view(["POST"])
@csrf_protect
def password_login(request:HttpRequest):

	logging.debug("Starting password login route.")
	form = LoginForm(request.POST)
	if form.is_valid():

		logging.debug("Verifying if user exists.")
		_, user = verify_exists_model(request, authenticate, **form.cleaned_data)
		if user is None or not user.is_active:
			logging.debug("Response status 404. User not founded.")
			return Response({"message":"User don't exists"}, status=status.HTTP_404_NOT_FOUND)

		logging.debug("Response status 200. User logged successful.")
		return generate_full_jwt_response(request, user)	
	
	logging.debug(f"Response status 400. Invalid credentials. Errors: {form.errors}")
	return Response({"message":"Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)	


@api_view(["POST"])
@csrf_protect
def password_register(request):

	logging.debug("Starting password register route.")
	register_form = RegisterForm(request.POST)

	logging.debug(f"Verifying if email and password are valids. Data: {register_form.data}")
	if not register_form.is_valid():
		logging.debug(f"Response 400. Invalid credentials. Errors: {register_form.errors}")
		return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

	logging.debug("Verifying if user already exists.")
	exists_user, _ = verify_exists_model(request, authenticate, **register_form.cleaned_data)
	if exists_user:
		logging.debug("Response 401. User already exists.")
		return Response({"message":"User already exists."}, status=status.HTTP_401_UNAUTHORIZED)
	
	user_form = UserRegisterExtras(request.POST)
	company_form = CompanyRegisterExtras(request.POST)

	logging.debug("Verifying if the user desire register a company.")
	if company_form.data.get("is_company")=="on":
		if not company_form.is_valid():
			logging.debug(f"Response status 400. Invalid company credentials.  Errors: {company_form.errors}")
			return Response({"message":"Invalid company credentials."}, status=status.HTTP_400_BAD_REQUEST)
		
		company_data = company_form.cleaned_data
		company_data.pop("is_company")
		
		logging.debug("Verifying if company already exists.")
		_, company_query = verify_exists_model(request, Company.objects.filter, **company_data)
		if company_query is None:
			logging.debug("Response status 500. Internal server error.")
			return Response({"message": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
		exists_company, _ = verify_exists_model(request, company_query.first)
		if exists_company:
			logging.debug("Response 401. Company already exists.")
			return Response({"message":"Company already exists."}, status=status.HTTP_401_UNAUTHORIZED)
		
		return register_company(request, {**company_data, **register_form.cleaned_data})
	
	logging.debug("Verifying if the user desire register a common user.")
	if user_form.is_valid():
		return register_user(request, {**user_form.cleaned_data, **register_form.cleaned_data})
	
	logging.debug(f"Response 400. Invalid credentials user credentials. Errors: {user_form.errors}")
	return Response({"message": "Invalid user credentials."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def logout(request:HttpRequest):

	response = redirect("http://localhost:3000")
	response.delete_cookie("refresh_token")
	return response
