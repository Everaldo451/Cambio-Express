from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse, HttpRequest
from rest_framework_simplejwt.authentication import JWTAuthentication
import logging
import os

print(__name__)
logger = logging.getLogger(__name__)


def JWTAuthenticationMiddleware(get_response):

    def middleware(request):

        jwt_auth = JWTAuthentication()
        obj = jwt_auth.authenticate(request)
        if obj is not None:
            user, token = obj
            print(user)
            request.user = user

        return get_response(request)
    
    return middleware


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

        endpoint:str = request.get_full_path()

        if endpoint.startswith("/"+os.environ.get("DJANGO_ADMIN_URL")):
            return get_response(request)
        
        method = request.method
        endpoint = request.get_full_path()


        user = request.user
        print(user)
        username = "anonymous"

        if user.is_authenticated:
            if user.is_superuser: 
                return get_response(request)
            username = user.username
        
        response = get_response(request)
        status = response.status_code

        extra = {
            "username":username, 
            "status": status, 
            "method": method,
            "endpoint": endpoint,
        }

        logger.info("Request:", extra=extra)

        return response

    return middleware
        
    