from rest_framework.authentication import BaseAuthentication
from .extras.jwt import cookie_authenticate
import logging


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        obj = cookie_authenticate(request)
        if obj is None:
            return None
        
        user, token = obj
        return (user, token)