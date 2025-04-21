from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token
from api.models import User

def generate_token_cookie(response:Response, token:Token, cookiename:str):
      response.set_cookie(cookiename, str(token), expires=token.lifetime, httponly=True)


def generate_token_cookies(response:Response, refresh_token:RefreshToken):
    generate_token_cookie(response, refresh_token, "refresh_token")
    generate_token_cookie(response, refresh_token.access_token, "access_token")
    

def generate_jwt_response_instance(refresh_token:RefreshToken):
	return Response({
        "data":{
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token)
		}
	})


def generate_full_jwt_response(request:HttpRequest|Request, user:User):
	refresh = RefreshToken.for_user(user)
	response = generate_jwt_response_instance(refresh)
	generate_token_cookies(response, refresh)
	return response