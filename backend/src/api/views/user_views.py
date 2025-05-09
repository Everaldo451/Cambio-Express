from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
import logging

from authe.serializers import RegisterSerializer
from authe.extras.register_company import register_company
from authe.extras.register_user import register_user
from authe.extras.generate_jwt_response import generate_full_jwt_response

from api.models import User, Company
from api.serializers.models import UserSerializer

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
	

	def create_company(self, request:HttpRequest, data:dict):
		data.pop("is_company")
		
		logging.debug("Verifying if company already exists.")
		if Company.objects.filter(CNPJ=data.get("CNPJ")).exists():
			logging.debug("Response 409. Company already exists.")
			return Response({"message":"Company already exists."}, status=status.HTTP_409_CONFLICT)
		
		return register_company(request, {**data})
	

	def create_user(self, request:HttpRequest, data:dict):
		register_data = register_user(request, {**data})
		if register_data["error"] == True:
			stat = register_data["status"]
			error = register_data["content"]
			logging.debug(f"Response with status {stat}. Error: {error}")
			return Response({"message": error}, status=stat)
		
		logging.debug(f"Response with status 201. User registed sucessful.")
		return generate_full_jwt_response(request, register_data["content"], status.HTTP_201_CREATED)
	

	@method_decorator(csrf_protect)
	def post(self, request:Request, format=None):
		logging.debug("Starting password register route.")
		serializer = RegisterSerializer(data=request.data)

		logging.debug(f"Verifying if email and password are valids.")
		if not serializer.is_valid():
			logging.debug(f"Response 400. Invalid credentials. Errors: {serializer.errors}")
			return Response({"message": "Invalid credentials.", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

		validated_data = serializer.validated_data
		logging.debug("Verifying if user already exists.")
		if User.objects.filter(email=validated_data.get("email")).exists():
			logging.debug("Response 409. User already exists. Conflict")
			return Response({"message":"User already exists."}, status=status.HTTP_409_CONFLICT)

		logging.debug("Verifying if the user desire register a company.")
		if validated_data["is_company"]:
			return self.create_company(request, validated_data)
		
		return self.create_user(request, validated_data)
	



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
