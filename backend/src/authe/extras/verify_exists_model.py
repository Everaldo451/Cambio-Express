from django.http import HttpRequest
from typing import Callable
import logging

def verify_exists_model(request:HttpRequest, verify_function:Callable, **data):

    model = verify_function(**data) if data else verify_function()
    logging.debug(f"Model: {model}")

    if model is not None: 
        return True, model
    return False, None