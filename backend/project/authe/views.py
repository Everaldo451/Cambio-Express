from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

from api.models import Company
from authe.models import User

from .form import LoginForm, UserRegisterExtras, CompanyRegisterExtras, RegisterForm, OAuthForm
from .serializers import UserSerializer

from .extras.generate_jwt_response import generate_full_jwt_response
from .extras.register_company import register_company
from .extras.register_user import register_user
from .extras.verify_exists_model import verify_exists_model
from .extras.generate_oauth_config import generate_oauth_config
from .extras.oauth_utils import check_granted_scopes

from googleapiclient.discovery import build
import google_auth_oauthlib.flow

import logging
from dotenv import load_dotenv

load_dotenv()

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request:HttpRequest):
	logging.debug(f"Getting the user data.")
	serializer = UserSerializer(request.user)
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
	redirect_uri = f"http://{request.get_host()}{reverse('oauth2callback')}"
	logging.debug(f"Redirect uri: {redirect_uri}")
	flow = google_auth_oauthlib.flow.Flow.from_client_config(**generate_oauth_config(request, redirect_uri))
	flow.redirect_uri = redirect_uri
	authorization_url, state = flow.authorization_url(access_type = 'offline',prompt="consent")
	request.session['state'] = state

	if authorization_url:
		logging.debug(f"Authorization url: {authorization_url}")
		return redirect(authorization_url)
	
	return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def oauth_callback(request:HttpRequest):
	oauth_form = OAuthForm(request.GET)
	if not oauth_form.is_valid():
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

		_, user_query = verify_exists_model(request, User.objects.filter, email=email)
		if user_query is None:
			return redirect("http://localhost:3000/oauth/fail?e='Internal server error.'")
		
		exists_user, user = verify_exists_model(request, user_query.first)
		if exists_user and user.is_active:
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
		register_data = register_user(request, {**user_form.cleaned_data, **register_form.cleaned_data})
		if register_data["error"] == True:
			stat = register_data["status"]
			error = register_data["content"]
			logging.debug(f"Response with status {stat}. Error: {error}")
			return Response({"message": error}, status=stat)
		
		logging.debug(f"Response with status 200. User registed sucessful.")
		return generate_full_jwt_response(request, register_data["content"])
	
	logging.debug(f"Response 400. Invalid user credentials. Errors: {user_form.errors}")
	return Response({"message": "Invalid user credentials."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def logout(request:HttpRequest):

	response = redirect("http://localhost:3000")
	response.delete_cookie("refresh_token")
	return response
