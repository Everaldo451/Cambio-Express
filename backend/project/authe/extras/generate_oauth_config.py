from django.urls import reverse
from django.http import HttpRequest
from dotenv import load_dotenv
import os

load_dotenv()

def generate_oauth_config(request:HttpRequest):
    client_id = os.getenv("OAUTH_CLIENT_ID")
    client_secret = os.getenv("OAUTH_CLIENT_SECRET")
    
    redirect_uri = reverse('oauth2callback')

    client_config = {
		"web": {
			"client_id": client_id,
			"client_secret": client_secret,
			"redirect_uris": [redirect_uri],
    		"auth_uri": "https://accounts.google.com/o/oauth2/auth",
    		"token_uri": "https://accounts.google.com/o/oauth2/token"
		}
	}
    
    scopes = ['https://www.googleapis.com/auth/userinfo.email',
		'https://www.googleapis.com/auth/userinfo.profile',
		'OpenID'
	]

    return {"client_config": client_config, "scopes": scopes}