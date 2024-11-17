from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token
from api.models import User

def generate_token_cookie(response:Response, token:Token, cookiename:str):
      response.set_cookie(cookiename, str(token), expires=token.lifetime, httponly=True)

def generate_token_cookies(response:Response, refresh_token:Token):

    generate_token_cookie(response, refresh_token, "refresh_token")
    generate_token_cookie(response, refresh_token.access_token, "access_token")
    

def generate_token_response(refresh_token:Token):
       
	print(refresh_token.access_token)
      
	return Response({
		"refresh": str(refresh_token),
		"access": str(refresh_token.access_token)
	})


def generate_tokens(request:HttpRequest|Request, user:User):

	refresh = RefreshToken.for_user(user)
	response = generate_token_response(refresh)

	generate_token_cookies(response, refresh)
      
	return response