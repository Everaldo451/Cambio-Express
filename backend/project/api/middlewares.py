from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.http import HttpResponse, HttpRequest
from api.models import User
from api.serializers import UserSerializer
import logging

print(__name__)
logger = logging.getLogger(__name__)

def RefreshJWT(get_response):

    def middleware(request):

        if request.COOKIES.get("refresh") and not request.COOKIES.get("access"):

            try:

                refresh = RefreshToken(request.COOKIES.get("refresh"))

                response = get_response(request)
                response.set_cookie("access",
                                    refresh.access_token,
                                    httponly=True,
                                    max_age=refresh.access_token.lifetime
                                    )
                return response
            
            except:

                response = get_response(request)
                return response
            
        else:
            response = get_response(request)
            return response
        
    return middleware

def LogRequest(get_response):

    def middleware(request):

        method = request.method
        endpoint = request.get_full_path()

        user = request.user
        username = user.username if user.is_authenticated else "anonymous"
        
        response = get_response(request)
        status = response.status_code

        extra = {
            "username":username, 
            "status": status, 
            "method": method,
            "endpoint": endpoint,
        }
        print(extra)

        logger.info("Request:", extra=extra)

        return response

    return middleware
        
    