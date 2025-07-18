from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from django.http import HttpRequest
from django.contrib.auth import authenticate

from users.models import User

from .serializers import PasswordLoginSerializer, PasswordLoginResponseSerializer

from authentication.services import JWTService

import logging

class PasswordLogin(APIView):

	jwt_service = JWTService()

	@swagger_auto_schema(
		request_body=PasswordLoginSerializer,
		responses={
			201:PasswordLoginResponseSerializer
		}
	)
	def post(self, request:HttpRequest|Request, format=None):
		logging.debug("Starting password login route.")
		serializer = PasswordLoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		user = serializer.validated_data['user']
		logging.debug("Response status 200. User logged successful.")
		return self.jwt_service.generate_response(request, user, status.HTTP_200_OK)
