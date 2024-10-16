from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponseBadRequest
from django.db import IntegrityError
from .models import User
from .serializers import UserSerializer
from .form import LoginForm, RegisterForm


serializer = UserSerializer()
request = HttpRequest()


@api_view(["POST"])
def login(request):

	form = LoginForm(request.POST)

	if form.is_valid():

		user = authenticate(
			request,
			username = form.cleaned_data.get("email"),
			password = form.cleaned_data.get("password")
			)

		if user is not None and user.is_active:

			response = redirect("/")
			refresh = RefreshToken.for_user(user)
			response.set_cookie("access",refresh.access_token,httponly=True,max_age=refresh.access_token.lifetime)
			response.set_cookie("refresh",refresh,httponly=True,max_age=refresh.lifetime)
			return response
			
		else:
			messages.error(request,"No user")
			return redirect("/login")
	
	else: return redirect("/login")
	

	

@api_view(["POST"])
def register(request):

	form = RegisterForm(request.POST)

	if form.is_valid():

		try:

			nuser = User.objects.create_user(form.cleaned_data.get("email"),form.cleaned_data.get("username"),form.cleaned_data.get("password"))
			refresh = RefreshToken.for_user(nuser)

			response = redirect("/")
					
			response.set_cookie("access",refresh.access_token,httponly=True,max_age=refresh.access_token.lifetime)
			response.set_cookie("refresh",refresh,httponly=True,max_age=refresh.lifetime)
			
			return response
				
		except IntegrityError as e:
			error = str(e)
			if error.startswith("UNIQUE"):
				if error.find('app.email'):
					messages.error(request,"email já existente")
				elif error.find('app.username'):
					messages.error(request,"username já existente")
				
			return redirect("/login")
	
	else: return redirect("/login")


def logout(request):

	response = redirect("/")
	response.delete_cookie("access")
	response.delete_cookie("refresh")

	return response
	
	