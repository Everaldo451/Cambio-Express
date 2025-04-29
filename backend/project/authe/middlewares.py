from django.http import HttpRequest
from rest_framework_simplejwt.tokens import RefreshToken
from .extras.generate_jwt_response import generate_token_cookies

def RefreshJWT(get_response):

    def middleware(request:HttpRequest):
        refresh_cookie = request.COOKIES.get("refresh_token")
        access_cookie = request.COOKIES.get("access_token")

        if refresh_cookie and not access_cookie:
            try:
                refresh_token = RefreshToken(refresh_cookie)
                response = get_response(request)
                generate_token_cookies(response, refresh_token)
                return response
            except:
                response = get_response(request)
                return response
        else:
            response = get_response(request)
            return response
        
    return middleware
