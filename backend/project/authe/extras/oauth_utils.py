from google.oauth2.credentials import Credentials

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