from google.oauth2.credentials import Credentials
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


##OAuth credentials:
##{
##	'token': credentials.token,
##	'refresh_token': credentials.refresh_token,
##	'token_uri': credentials.token_uri,
##	'client_id': credentials.client_id,
##	'client_secret': credentials.client_secret,
##	'granted_scopes': credentials.granted_scopes
##}
def check_granted_scopes(credentials:Credentials):
    features = {}
    if 'https://www.googleapis.com/auth/userinfo.email' in credentials.granted_scopes:
        features["email"] = True
        
    if 'https://www.googleapis.com/auth/userinfo.profile' in credentials.granted_scopes:
        features["profile"] = True

    if 'openid' in credentials.granted_scopes:
        features["openid"] = True

    return features