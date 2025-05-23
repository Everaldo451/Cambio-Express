from django.http import HttpRequest

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
import logging

from core.db import get_obj_by_id, get_all_obj

from users.models import User
from users.serializers.models import UserSerializer


class UserList(APIView):

	def get_permissions(self,):
		return [IsAdminUser()]

	def get(self, request:HttpRequest, format=None):
		get_users_data = get_all_obj(User)
		if get_users_data["error"]:
			return Response({"message":get_users_data["message"]},status=get_users_data["status"])
		
		users = get_users_data["obj"]
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=get_users_data["status"])
	


class UserDetails(APIView):

	permission_classes = [IsAdminUser]

	def get(self, request:HttpRequest, id:int, format:None):
		logging.debug(f"Getting the user data.")
		get_user_data = get_obj_by_id(User, id)
		if get_user_data["error"]:
			return Response({"message":get_user_data["message"]},status=get_user_data["status"])
		
		user:User = get_user_data["obj"]
		serializer = UserSerializer(user)

		logging.debug(f"Response status 200. User data: {serializer.data}")
		return Response(serializer.data, status=get_user_data["status"])
