from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from .models import User
from .serializers import UserSerializer
from .form import LoginForm, RegisterForm
from django.utils import timezone
from datetime import datetime

serializer = UserSerializer()
request = HttpRequest()

def login(request):

	if request.method == "POST":

		form = LoginForm(request.POST)

		if form.is_valid():

			user = authenticate(request,username = form.cleaned_data.get("email"),password = form.cleaned_data.get("password"))

			if user:

				response = redirect("/")
				serializer = UserSerializer(user)
				refresh = RefreshToken()
				refresh.payload = {"id":serializer.data.get("id")}
				response.set_cookie("access",refresh.access_token,httponly=True,expires=timezone.now()+refresh.lifetime)
				response.set_cookie("refresh",refresh,httponly=True,expires=timezone.now()+refresh.access_token.lifetime)
				return response
			
			else:
				messages.error(request,"No user")
				return redirect("/login")
	
		else: return redirect("/login")
	
	else: return HttpResponseBadRequest("Method not allowed")
	

	


def register(request):

	form = RegisterForm(request.POST)

	if form.is_valid():

		user = authenticate(request,username = form.cleaned_data.get("email") ,password = form.cleaned_data.get("password"))

		if user:

			messages.error(request,"Usuario ja existe")
			return redirect("/login")
	
		else:

			nuser = User.objects.create_user(form.cleaned_data.get("email"),form.cleaned_data.get("username"),form.cleaned_data.get("password"))
			serializer = UserSerializer(nuser)
			response = HttpResponse(redirect("/",user=serializer.data))
			response.set_cookie("access",serializer.data)
			
			return response
	
	else: return redirect("/login")