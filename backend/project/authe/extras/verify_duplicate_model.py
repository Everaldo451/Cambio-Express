from api.models import Company
from django.http import HttpRequest
from django.contrib.auth import authenticate

def verify_duplicate_model(request:HttpRequest, verify_function:function, **data):

    model = verify_function(**data)

    if model: 
        return True
    return False