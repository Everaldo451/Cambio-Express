from django.http import HttpRequest
from django.middleware.csrf import get_token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token

from users.serializers.models import UserSerializer
from users.models import User
import logging


class JWTService:

    def generate_token_data(self, request:HttpRequest|Request, token:Token):
        return {
            "value": str(token),
            "lifetime": token.lifetime
        }


    def generate_tokens_data(self, request:HttpRequest|Request, user:User):
        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        return {
            "refresh_token": self.generate_token_data(request, refresh_token),
            "access_token": self.generate_token_data(request, access_token)
        }


    def generate_response(self, request:HttpRequest|Request, user:User, status:int):
        logging.debug("Generating JWT Response")
        serializer = UserSerializer(user)
        return Response(
            {
                "message":"Authenticated successful.",
                "data": { 
                    "user": serializer.data,
                    "tokens": {
                        "csrf_token": get_token(request),
                        **self.generate_tokens_data(request, user) 
                    }
                }
            },
            status=status
        )