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
from django.db import DatabaseError, transaction
from django.views.decorators.csrf import csrf_protect
from .models import User
from .form import LoginForm, RegisterFormForCompany, RegisterFormForUser
from .utils import generate_tokens, generate_token_response
from .serializers import UserSerializer
from extras import register_company, register_user


@api_view(["GET"])
def get_jwt(request):

	if request.COOKIES.get("refresh_token"):
		try:
			refresh = RefreshToken(request.COOKIES.get("refresh_token"), True)
			return generate_token_response(refresh)
		except TokenError as err: 
			print(err.args)
			return Response(None)
	return Response(None)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
	
	serializer = UserSerializer(request.user)
	if not serializer.is_valid():
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	data = serializer.data
	data.pop("id")
	if not request.user.groups.filter(name="Company").exists():
		print("notCompany")
		data.pop("company")

	return Response(data)


@api_view(["POST"])
@csrf_protect
def oauthLogin(request):
	pass


	
@api_view(["POST"])
@csrf_protect
def login(request):

	form = LoginForm(request.POST)

	if form.is_valid():

		user = authenticate(
			request,
			username = form.cleaned_data.get("email"),
			password = form.cleaned_data.get("password")
		)

		if user is None or not user.is_active:

			print("No user")
			return Response("No user", status=status.HTTP_401_UNAUTHORIZED)

		return generate_tokens(request, user)
		
	
	return Response(None, status=status.HTTP_401_UNAUTHORIZED)	


@api_view(["POST"])
@csrf_protect
def register(request):

	user_form = RegisterFormForUser(request.POST)
	company_form = RegisterFormForCompany(request.POST)

	if company_form.is_valid():
		return register_company.func(request, company_form)
	
	elif user_form.is_valid():
		return register_user.func(request, user_form)
	else: 
		print("not valid")
		return Response(None, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def logout(request):

	response = redirect("http://localhost:3000")
	response.delete_cookie("refresh_token")

	return response
