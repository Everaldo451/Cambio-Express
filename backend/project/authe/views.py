from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.db import IntegrityError, transaction
from django.views.decorators.csrf import csrf_protect
from api.models import Company
from .models import User
from .form import LoginForm, RegisterFormForCompany, RegisterFormForUser
from .utils import generate_tokens, generate_token_response
from .serializers import UserSerializer
from django.http import HttpRequest


@api_view(["GET"])
def get_jwt(request):

	if request.COOKIES.get("refresh_token"):
		try:
			
			refresh = RefreshToken(request.COOKIES.get("refresh_token"))
			return generate_token_response(refresh)
		
		except: return Response(None)
	return Response(None)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):

	try:
		serializer = UserSerializer(request.user)
		serializer = serializer.data
		serializer.pop("id")
		if not request.user.groups.filter(name="Company").exists():
			print("notCompany")
			serializer.pop("company")

		return Response(serializer)

	except Exception as e: 
		return Response(None)
	

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


	if formForCompany.is_valid():

		user_data = formForCompany.cleaned_data

		try:

			with transaction.atomic():

				user = User.objects.create_user(
					email = user_data.pop("email"),
					password= user_data.pop("password")
				)

				company = Company(**user_data,user = user)
				company.save()

			return generate_tokens(request, user)
				
		except:

			return Response(None, status=status.HTTP_400_BAD_REQUEST)
	
	elif formForUser.is_valid():

		user_data = formForUser.cleaned_data

		try:

			full_name = user_data.get("full_name")

			splited = full_name.split(maxsplit=1)
			first_name  = splited[0]
			last_name = splited[1]

			user = User.objects.create_user(

				email=formForCompany.cleaned_data.get("email"),
				password = formForCompany.cleaned_data.get("password"),
				first_name = first_name,
				last_name = last_name
			)

			return generate_tokens(request, user)
		
		except IndexError as e:
			return Response({"Insira um nome completo"}, status=status.HTTP_400_BAD_REQUEST)
		except IntegrityError as e:
			return Response(None, status=status.HTTP_400_BAD_REQUEST)
	else: 
		print("not valid")
		return Response(None, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def logout(request):

	response = redirect("http://localhost:3000")
	response.delete_cookie("refresh_token")

	return response
	
	

# Create your views here.
