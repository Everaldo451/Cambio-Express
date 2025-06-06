from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import logging

from users.serializers.models import UserSerializer
from users.serializers.use_cases import UpdateUserSerializer

class MeDetails(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request:HttpRequest|Request, format=None):
		logging.debug("Getting authenticated user data.")
		serializer = UserSerializer(request.user)
			
		logging.debug(f"Response status 200. User data: {serializer.data}")
		return Response(serializer.data, status=status.HTTP_200_OK)
	

	def patch(self, request:HttpRequest|Request, format=None):
		logging.debug("Modifying authenticated user data")
		serializer = UpdateUserSerializer(instance=request.user, data=request.data, partial=True)

		if not serializer.is_valid():
			logging.debug("Response status 400. Bad request")
			return Response(
				{
					"message":"Invalid data. Bad Request.",
					"errors":serializer.errors
				}, 
				status=status.HTTP_400_BAD_REQUEST
			)
		
		user = serializer.save()
		serializer = UserSerializer(user)
		logging.debug("Response status 200. Authenticated user updated successful.")
		return Response(serializer.data, status=status.HTTP_200_OK
		)
