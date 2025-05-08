from django.http import HttpRequest
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
import logging

from authe.form import RegisterForm, CompanyRegisterExtras, UserRegisterExtras
from authe.extras.register_company import register_company
from authe.extras.register_user import register_user
from authe.extras.generate_jwt_response import generate_full_jwt_response

from api.models import User, Company
from api.serializers import UserSerializer

class UserList(APIView):

	def get_permissions(self,):
		if self.request.method == "POST":
			return []
		return [IsAdminUser]

	def get(self, request:HttpRequest, format=None):
		users = None
		try:
			users = User.objects.all()
		except Exception as error:
			return Response({"message":"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
		serializer = UserSerializer(users)
		return Response(serializer.data, status=status.HTTP_200_OK)
	

	def create_company(self, request:HttpRequest, register_form:RegisterForm, company_form:CompanyRegisterExtras):
		company_data = company_form.cleaned_data
		company_data.pop("is_company")
		
		logging.debug("Verifying if company already exists.")
		company = Company.objects.filter(**company_data).first()
		if company is not None:
			logging.debug("Response 401. Company already exists.")
			return Response({"message":"Company already exists."}, status=status.HTTP_401_UNAUTHORIZED)
		
		return register_company(request, {**company_data, **register_form.cleaned_data})
	

	def create_user(self, request:HttpRequest, register_form:RegisterForm, user_form:UserRegisterExtras):
		register_data = register_user(request, {**user_form.cleaned_data, **register_form.cleaned_data})
		if register_data["error"] == True:
			stat = register_data["status"]
			error = register_data["content"]
			logging.debug(f"Response with status {stat}. Error: {error}")
			return Response({"message": error}, status=stat)
		
		logging.debug(f"Response with status 200. User registed sucessful.")
		return generate_full_jwt_response(request, register_data["content"])
	

	def post(self, request:HttpRequest, format=None):
		logging.debug("Starting password register route.")
		register_form = RegisterForm(request.POST)

		logging.debug(f"Verifying if email and password are valids. Data: {register_form.data}")
		if not register_form.is_valid():
			logging.debug(f"Response 400. Invalid credentials. Errors: {register_form.errors}")
			return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

		logging.debug("Verifying if user already exists.")
		user = authenticate(**register_form.cleaned_data)
		if user:
			logging.debug("Response 401. User already exists.")
			return Response({"message":"User already exists."}, status=status.HTTP_401_UNAUTHORIZED)
	
		user_form = UserRegisterExtras(request.POST)
		company_form = CompanyRegisterExtras(request.POST)

		logging.debug("Verifying if the user desire register a company.")
		if company_form.data.get("is_company")=="on":
			if not company_form.is_valid():
				logging.debug(f"Response status 400. Invalid company credentials.  Errors: {company_form.errors}")
				return Response({"message":"Invalid company credentials."}, status=status.HTTP_400_BAD_REQUEST)
		
			return self.create_company(request, register_form, company_form)
	
		logging.debug("Verifying if the user desire register a common user.")
		if not user_form.is_valid():
			logging.debug(f"Response 400. Invalid user credentials. Errors: {user_form.errors}")
			return Response({"message": "Invalid user credentials."}, status=status.HTTP_400_BAD_REQUEST)
		
		return self.create_user(request, register_form, user_form)
	



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
