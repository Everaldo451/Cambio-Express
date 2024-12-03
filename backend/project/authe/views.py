from dotenv import load_dotenv
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import AbstractUser

from api.models import Company

from .form import LoginForm, UserRegisterExtras, CompanyRegisterExtras, RegisterForm, OAuthForm
from .utils import generate_tokens, generate_token_response
from .serializers import UserSerializer

from extras.register_company import register_company
from extras.register_user import register_user
from extras.verify_exists_model import verify_exists_model

import google.oauth2.credentials
import google_auth_oauthlib.flow

load_dotenv()


@api_view(["GET"])
def get_jwt(request):

	token_string = request.COOKIES.get("refresh_token")

	if token_string is not None:
		try:
			refresh_token = RefreshToken(token_string)
			return generate_token_response(refresh_token)
		except TokenError as err: 
			print(err.args)
			return Response({"message":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
		
	return Response({"message":"Token not provided"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def oauth_client_url(request):

	client_id = os.getenv("OAUTH_CLIENT_ID")
	client_secret = os.getenv("OAUTH_CLIENT_SECRET")

	redirect_uri = 'http://localhost/auth/oauth2callback'

	client_config = {
		"web": {
			"client_id": client_id,
			"client_secret": client_secret,
			"redirect_uris": [redirect_uri],
    		"auth_uri": "https://accounts.google.com/o/oauth2/auth",
    		"token_uri": "https://accounts.google.com/o/oauth2/token"
		}
	}

	scopes = ['https://www.googleapis.com/auth/userinfo.email',
		'https://www.googleapis.com/auth/userinfo.profile',
		'OpenID'
	]

	flow = google_auth_oauthlib.flow.Flow.from_client_config(client_config, scopes)

	flow.redirect_uri = redirect_uri
	
	client_id = os.getenv("OAUTH_CLIENT_ID")

	if client_id is not None:
		return Response({"data":client_id}, status=status.HTTP_200_OK)
	
	return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def oauth_login(request):

	oauth_form = OAuthForm(request.GET)

	if oauth_form.is_valid():

		return
	pass


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
	
	serializer = UserSerializer(request.user)
	if not serializer.is_valid():
		return Response({"message":"Internal server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	
	data = serializer.data
	
	if not request.user.groups.filter(name="Company").exists():
		print("notCompany")
		data.pop("company")

	data.pop("id")

	return Response(data)

	
@api_view(["POST"])
@csrf_protect
def login(request):

	form = LoginForm(request.POST)
	if form.is_valid():

		_, user = verify_exists_model(request, authenticate, **form.cleaned_data)

		if not isinstance(user, AbstractUser) or not user.is_active:
			return Response({"message":"User don't exists"}, status=status.HTTP_401_UNAUTHORIZED)

		return generate_tokens(request, user)	
	
	print(form.errors)
	return Response({"messages":"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)	



@api_view(["POST"])
@csrf_protect
def register(request):

	register_form = RegisterForm(request.POST)
	user_form = UserRegisterExtras(request.POST)
	company_form = CompanyRegisterExtras(request.POST)

	if register_form.is_valid():
		register_data = register_form.cleaned_data

		exists_user, _ = verify_exists_model(request, authenticate, **register_data)
		if exists_user:
			return Response({"message":"User already exists"}, status=status.HTTP_401_UNAUTHORIZED)
	else:
		print(register_form.errors)
		return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
	

	if company_form.is_valid():
		company_data = company_form.cleaned_data
		company_data.pop("is_valid")
		
		exists_company, _ = verify_exists_model(request, Company.objects.filter, **company_data)
		if exists_company:
			return Response({"message":"Company already exists"}, status=status.HTTP_401_UNAUTHORIZED)
		
		return register_company(request, {**company_data, **register_data})
	
	elif user_form.is_valid():
		return register_user(request, {**user_form.cleaned_data, **register_data})
	
	
	print(register_form.errors)
	return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def logout(request):

	response = redirect("http://localhost:3000")
	response.delete_cookie("refresh_token")

	return response
