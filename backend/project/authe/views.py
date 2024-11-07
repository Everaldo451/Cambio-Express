from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect
from api.models import User
from api.serializers import UserSerializer
from .form import LoginForm, RegisterForm


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

		if user is not None and user.is_active:

			refresh = RefreshToken.for_user(user)
			response = {
				"refresh": str(refresh),
				"access": str(refresh.access_token)
			}
			return Response(response)
			
		else:
			print("No user")
			messages.error(request,"No user")
			return Response(None, status=status.HTTP_401_UNAUTHORIZED)
	
	else: return Response(None, status=status.HTTP_401_UNAUTHORIZED)
	

	

@api_view(["POST"])
@csrf_protect
def register(request):

	form = RegisterForm(request.POST)

	if form.is_valid():

		try:

			nuser = User.objects.create_user(form.cleaned_data.get("email"),form.cleaned_data.get("username"),form.cleaned_data.get("password"))
			refresh = RefreshToken.for_user(nuser)

			response = {
				"refresh": str(refresh),
				"access": str(refresh.access_token)
			}

			print("ola")
			return Response(response)
				
		except IntegrityError as e:
			error = str(e)

			print(e)
			if error.startswith("UNIQUE"):
				if error.find('app.email'):
					messages.error(request,"email já existente")
				elif error.find('app.username'):
					messages.error(request,"username já existente")
				
			return Response(None, status=status.HTTP_400_BAD_REQUEST)
	
	else: 
		print("not valid")
		return Response(None, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def logout(request):

	response = redirect("http://localhost:3000")
	response.delete_cookie("access")
	response.delete_cookie("refresh")

	return response
	
	

# Create your views here.
