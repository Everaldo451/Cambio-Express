from django.http import HttpRequest

from .registers.common_user_register import CommonUserRegister
from .registers.company_user_register import CompanyUserRegister

from .response_creators import ResponseCreator
from .response_creators.common_user_response import CommonUserResponseCreator
from .response_creators.company_user_response import CompanyUserResponseCreator

from authentication.services import JWTService

def get_register_response_creator(request:HttpRequest, jwt_service:JWTService, validated_data:dict) -> ResponseCreator:
		if validated_data["is_company"]:
			return CompanyUserResponseCreator(jwt_service, CompanyUserRegister())
		return CommonUserResponseCreator(jwt_service, CommonUserRegister())