from django.urls import reverse
from django.http import HttpRequest
from dotenv import load_dotenv
import os


def generate_oauth_config(request:HttpRequest, redirect_uri:str):
    load_dotenv()
    client_id = os.getenv("OAUTH_CLIENT_ID")
    client_secret = os.getenv("OAUTH_CLIENT_SECRET")
    client_config = {
		"web": {
			"client_id": client_id,
			"client_secret": client_secret,
			"redirect_uris": [redirect_uri],
    		"auth_uri": "https://accounts.google.com/o/oauth2/auth",
    		"token_uri": "https://accounts.google.com/o/oauth2/token"
		}
	}
    scopes = ['openid','https://www.googleapis.com/auth/userinfo.email','https://www.googleapis.com/auth/userinfo.profile']

    return {"client_config": client_config, "scopes": scopes}