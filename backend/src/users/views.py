from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
import logging

from users.models import User
from users.serializers.models import UserSerializer


class UserList(APIView):

	def get_permissions(self,):
		if self.request.method == "POST":
			return []
		return [IsAdminUser()]

	def get(self, request:HttpRequest, format=None):
		users = None
		try:
			users = User.objects.all()
		except Exception as error:
			return Response({"message":"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
		serializer = UserSerializer(users)
		return Response(serializer.data, status=status.HTTP_200_OK)
	


class UserDetails(APIView):

	permission_classes = [IsAdminUser]

	def get(self, request:HttpRequest, id:int, format:None):
		logging.debug(f"Getting the user data.")
		user = None
		try:
			user = User.objects.get(id=id)
		except Exception as error:
			return Response({"message": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
		serializer = UserSerializer(user)
		data = serializer.data

		if not request.user.groups.filter(name="Company").exists():
			logging.debug("User isn't a company.")
			data.pop("company")

		logging.debug(f"Response status 200. User data: {data}")
		return Response({"data":data})
