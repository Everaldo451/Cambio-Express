from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect
from api.models import User, Company
from .form import LoginForm, RegisterFormForCompany, RegisterFormForUser
from .utils import generate_tokens
from django.http import HttpRequest
	

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

			return generate_tokens(request, user)
			
		else:
			print("No user")
			messages.error(request,"No user")
			return Response(None, status=status.HTTP_401_UNAUTHORIZED)
	
	else: return Response(None, status=status.HTTP_401_UNAUTHORIZED)
	

	

@api_view(["POST"])
@csrf_protect
def register(request):

	formForUser = RegisterFormForUser(request.POST)
	formForCompany = RegisterFormForCompany(request.POST)


	if formForUser.is_valid():

		try:

			first_name = ""
			last_name = ""

			full_name = formForUser.cleaned_data.get("full_name")
			if type(full_name) == str:
				splited_name = full_name.split(maxsplit=1)

				first_name = splited_name[0]
				last_name = splited_name[1]

			nuser = User.objects.create_user(
				email=formForUser.cleaned_data.get("email"),
				password = formForUser.cleaned_data.get("password"),
				first_name = first_name,
				last_name = last_name
			)

			return generate_tokens(request, nuser)
				
		except IntegrityError as e:
			error = str(e)
			return Response(None, status=status.HTTP_400_BAD_REQUEST)
	
	elif formForCompany.is_valid():

		try:

			nuser = User.objects.create_user(
				email=formForCompany.cleaned_data.get("email"),
				password = formForCompany.cleaned_data.get("password")
			)
			
			ncompany = Company(
				user = nuser,
				name = formForCompany.cleaned_data.get("name"),
				CNPJ = formForCompany.cleaned_data.get("CNPJ")
			)
			ncompany.save()

			return generate_tokens(request, nuser)
		
		except: pass
	else: 
		print("not valid")
		return Response(None, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def logout(request):

	response = redirect("http://localhost:3000")
	response.delete_cookie("access_token")
	response.delete_cookie("refresh_token")

	return response
	
	

# Create your views here.
