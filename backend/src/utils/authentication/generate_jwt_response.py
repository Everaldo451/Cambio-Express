from django.http import HttpRequest
from django.middleware.csrf import get_token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token
import logging

def generate_token_cookie(response:Response, token:Token, cookiename:str):
    logging.debug(f"JWT cookie {cookiename}: {str(token)}")
    response.set_cookie(cookiename, str(token), expires=token.lifetime, httponly=True)


def generate_token_cookies(response:Response, refresh_token:RefreshToken):
    generate_token_cookie(response, refresh_token, "refresh_token")
    generate_token_cookie(response, refresh_token.access_token, "access_token")
    

def generate_jwt_response_instance(request:HttpRequest|Request, refresh_token:RefreshToken, status:int):
    logging.debug("Generating JWT Response")
    return Response({"message":"Authenticated successful.", "csrf_token": get_token(request)}, status=status)


def generate_full_jwt_response(request:HttpRequest|Request, user, status:int):
    logging.debug("Generating the token")
    refresh = RefreshToken.for_user(user)
    response = generate_jwt_response_instance(request, refresh, status)
    generate_token_cookies(response, refresh)
    return response