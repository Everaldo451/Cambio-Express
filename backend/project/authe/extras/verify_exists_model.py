from django.http import HttpRequest
from typing import Callable

def verify_exists_model(request:HttpRequest, verify_function:Callable, **data):

    model = verify_function(**data)

    if model is not None: 
        return True, model
    return False, None