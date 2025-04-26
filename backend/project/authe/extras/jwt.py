from django.conf import settings
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.settings import api_settings


def cookie_authenticate(request:HttpRequest):
    cookie_name = "access_token"
    token_cookie = request.COOKIES.get(cookie_name)

    try:
        User = get_user_model()
        access_token = AccessToken(token_cookie)
        id = access_token.payload.get(api_settings.USER_ID_CLAIM)
        user = User.objects.get(int(id))
        if not user.is_active:
            return None
        
        return user, access_token
    except:
        return None
