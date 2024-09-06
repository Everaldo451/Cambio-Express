from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

def refresh_verify(get_response):

    def middleware(request):

        if not request.COOKIES.get("access") and request.COOKIES.get("refresh"):

               try:
                print(timezone.now())
                refresh = RefreshToken(request.COOKIES.get("refresh"))

                response = get_response(request)
                response.set_cookie("access",refresh.access_token,httponly=True,max_age=refresh.access_token.lifetime)

                return response
               
               except Exception as e: 
                  print(e)
                  return get_response(request)

        else: return get_response(request)
    
    return middleware