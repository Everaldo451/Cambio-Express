from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from users.models import User
from companies.models import Company

from .serializers import PasswordLoginSerializer, PasswordRegisterSerializer

from authentication.services import register_common_user, register_company_user
from authentication.services import JWTService

import logging


class PasswordRegister(APIView):

	jwt_service = JWTService()

	def company_exists(self, request:HttpRequest, data:dict):
		return Company.objects.filter(
			CNPJ=data.get("CNPJ")
		).exists()

	
	def create_company_user_and_response(self, request:HttpRequest, data:dict):
		data.pop("is_company")
		logging.debug("Verifying if company already exists.")
		if self.company_exists(request, data):
			logging.debug("Response 409. Company already exists.")
			return Response({"message":"Company already exists."}, status=status.HTTP_409_CONFLICT)
		
		register_data = register_company_user(request, {**data})
		if register_data["error"] == True:
			logging.debug(f"Response with error: {register_data["message"]}")
			return Response({"message": register_data["message"]}, status=register_data["status"])
		
		company:Company = register_data["obj"]
		return self.jwt_service.generate_response(request, company.user, status.HTTP_201_CREATED)
	

	def create_common_user_and_response(self, request:HttpRequest, data:dict):
		register_data = register_common_user(request, {**data})
		if register_data["error"] == True:
			logging.debug(f"Response with error: {register_data["message"]}")
			return Response({"message": register_data["message"]}, status=register_data["status"])
		
		logging.debug(f"Response with status 201. User registed sucessful.")
		user = register_data["obj"]
		return self.jwt_service.generate_response(request, user, status.HTTP_201_CREATED)
	

	@method_decorator(csrf_protect)
	def post(self, request:Request, format=None):
		logging.debug("Starting password register route.")
		serializer = PasswordRegisterSerializer(data=request.data)

		logging.debug(f"Verifying if email and password are valids.")
		if not serializer.is_valid():
			logging.debug(f"Response 400. Invalid credentials. Errors: {serializer.errors}")
			return Response({"message": "Invalid credentials.", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

		logging.debug("Verifying if user already exists.")
		validated_data = serializer.validated_data
		if User.objects.filter(email=validated_data.get("email")).exists():
			logging.debug("Response 409. User already exists. Conflict")
			return Response({"message":"User already exists."}, status=status.HTTP_409_CONFLICT)

		logging.debug("Verifying if the user desire register a company.")
		user=None
		if validated_data["is_company"]:
			return self.create_company_user_and_response(request, validated_data)
		return self.create_common_user_and_response(request, validated_data)



class PasswordLogin(APIView):

	jwt_service = JWTService()

	@method_decorator(csrf_protect)
	def post(self, request:HttpRequest|Request, format=None):
		logging.debug("Starting password login route.")
		serializer = PasswordLoginSerializer(data=request.data)
		if not serializer.is_valid():
			logging.debug(f"Response status 400. Invalid credentials. Errors: {serializer.errors}")
			return Response({"message":"Invalid credentials", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)	

		logging.debug("Verifying if user exists.")
		user = authenticate(**serializer.validated_data)
		if user is None:
			logging.debug(f"Response status 404. User not founded.")
			return Response({"message":"User don't exists"}, status=status.HTTP_404_NOT_FOUND)
		elif not user.is_active:
			logging.debug(f"Response status 403. Forbidden")
			return Response({"message":"The user isn't active"}, status=status.HTTP_403_FORBIDDEN)

		logging.debug("Response status 200. User logged successful.")
		return self.jwt_service.generate_response(request, user, status.HTTP_200_OK)
