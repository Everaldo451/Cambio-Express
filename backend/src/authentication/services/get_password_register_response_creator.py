from django.http import HttpRequest

from authentication.registers.common_user_register import CommonUserRegister
from authentication.registers.company_user_register import CompanyUserRegister

from authentication.password.response_creators import ResponseCreator
from authentication.password.response_creators.common_user_response import CommonUserResponseCreator
from authentication.password.response_creators.company_user_response import CompanyUserResponseCreator

from .jwt_service import JWTService

def get_register_response_creator(request:HttpRequest, jwt_service:JWTService, validated_data:dict) -> ResponseCreator:
		if validated_data["is_company"]:
			return CompanyUserResponseCreator(jwt_service, CompanyUserRegister())
		return CommonUserResponseCreator(jwt_service, CommonUserRegister())