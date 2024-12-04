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
from django.urls import reverse
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
from extras.generate_oauth_config import generate_oauth_config

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

	return Response({"data":data})

@api_view(["GET"])
def oauth_client_url(request):

	redirect_uri = reverse('oauth2callback')

	flow = google_auth_oauthlib.flow.Flow.from_client_config(**generate_oauth_config(request))

	flow.redirect_uri = redirect_uri
	
	authorization_url, state = flow.authorization_url(access_type = 'offline',prompt="consent")

	request.session['state'] = state

	if authorization_url:
		return Response({"url":authorization_url})
	
	return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def oauth_callback(request):

	oauth_form = OAuthForm(request.GET)

	if not oauth_form.is_valid():
		return Response({"message":"OAuth response is invalid"}, status=status.HTTP_400_BAD_REQUEST)
	

	redirect_uri = reverse('oauth2callback')

	rq = HttpRequest()

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
