from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from .models import UserManager
from .serializers import UserSerializer
from .form import LoginForm, RegisterForm

serializer = UserSerializer()
manager = UserManager()
request = HttpRequest()

@api_view(["POST"])
def login(request):

	form = LoginForm(request.POST)

	if form.is_valid():

		user = authenticate(request,username = form.email,password = form.password)

		if user:
			serializer = UserSerializer(user)
			response = HttpResponse(redirect("home",user=serializer))
			response.set_cookie("access",serializer)
			return response
		else:
			messages.error(request,"No user")
			return redirect(request.get_full_path())
	
	else: return redirect(request.get_full_path())
	

	

@api_view(["POST"])
def register(request):

	form = RegisterForm(request.POST)

	if form.is_valid():

		user = authenticate(request,username = form.email ,password = form.password)

		if user:

			messages.error(request,"Usuario ja existe")
			return redirect(request.get_full_path())
	
		else:

			nuser = manager.create_user(form.email,form.username,form.password)
			serializer = UserSerializer(nuser)
			response = HttpResponse(redirect("home",user=serializer))
			response.set_cookie("access",serializer)
			
			return response
	
	else: return redirect(request.get_full_path())