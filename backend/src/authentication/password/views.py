from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpRequest
from django.contrib.auth import authenticate

from users.models import User

from .serializers import PasswordLoginSerializer, PasswordRegisterSerializer

from authentication.services import JWTService
from authentication.services import get_register_response_creator

import logging


class PasswordRegister(APIView):

	jwt_service = JWTService()

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
		response_creator = get_register_response_creator(request, self.jwt_service, validated_data)
		return response_creator.create_response(request, validated_data)



class PasswordLogin(APIView):

	jwt_service = JWTService()

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
