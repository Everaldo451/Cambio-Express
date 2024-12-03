from api.models import Company
from django.http import HttpRequest
from django.contrib.auth import authenticate

def verify_exists_model(request:HttpRequest, verify_function:function, **data):

    model = verify_function(**data)

    if model is not None: 
        return True, model
    return False, None