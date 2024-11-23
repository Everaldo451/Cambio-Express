from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse, HttpRequest
from rest_framework_simplejwt.authentication import JWTAuthentication


def JWTAuthenticationMiddleware(get_response):

    def middleware(request):

        jwt_auth = JWTAuthentication()
        obj = jwt_auth.authenticate(request)
        if obj is not None:
            user, token = obj
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
