from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import logging

from api.serializers import UserSerializer

class MeDetails(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request:HttpRequest, format=None):
		logging.debug(f"Getting the user data.")
		serializer = UserSerializer(request.user)
		data = serializer.data
		data.pop("id")
		
		if not request.user.groups.filter(name="Company").exists():
			logging.debug("User isn't a company.")
			print("notCompany")
			data.pop("company")
			
		logging.debug(f"Response status 200. User data: {data}")
		return Response(data, status=status.HTTP_200_OK)
