from django.http import HttpRequest, HttpResponse
from django.db import DatabaseError
from authe.models import User
from rest_framework.response import Response
from rest_framework import status

from .generate_jwt_response import generate_full_jwt_response
import logging

def register_user(request:HttpRequest, user_data:dict) -> HttpResponse | Response:
    
    logging.debug("Creating the company")
    try:
        full_name = user_data.get("full_name")
        splited = full_name.split(maxsplit=1)
        first_name  = splited[0]
        last_name = splited[1]
        
        user = User.objects.create_user(
			email=user_data.get("email"),
			password = user_data.get("password"),
			first_name = first_name,
			last_name = last_name
		)
        
        return generate_full_jwt_response(request, user)
    except IndexError as err:
        logging.debug(f"Index error. Invalid full name. Error: {err.args}")
        return Response({"Insira um nome completo"}, status=status.HTTP_400_BAD_REQUEST)
    except DatabaseError as err:
        logging.debug("Internal server error. Database error.")
        return Response({"message":"An internal error ocurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    