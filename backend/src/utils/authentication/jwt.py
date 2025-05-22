from django.http import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.settings import api_settings
import logging


def cookie_authenticate(request:HttpRequest):
    logging.debug("Starting cookie authenticate")
    cookie_name = "access_token"
    token_cookie = request.COOKIES.get(cookie_name)
    
    try:
        User = get_user_model()
        logging.debug("Generate access token")
        access_token = AccessToken(token_cookie)
        id = access_token.payload.get(api_settings.USER_ID_CLAIM)
        logging.debug(f"Search user by id. ({id})")
        user = User.objects.get(id=int(id))
        if not user.is_active:
            logging.debug("Fail: unactived user.")
            return None
        
        logging.debug("User fetch sucessful.")
        return user, access_token
    except Exception as error:
        logging.debug(f"Fail: {error}")
        return None
