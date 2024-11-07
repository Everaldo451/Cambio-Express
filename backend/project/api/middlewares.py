from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from api.models import User
from api.serializers import UserSerializer

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
        
    