from django.http import HttpRequest
from django.db import DatabaseError
from authe.models import User
from rest_framework import status
import logging

def register_for_oauth(request:HttpRequest, user_data:dict) -> User:
    user = User.objects.create(
        email=user_data.get("email"),
        authentication_type=user_data.get("authentication_type")
    )

    return user

def register_for_password(request:HttpRequest, user_data:dict) -> User:
    full_name:str = user_data.get("full_name")
    splited = full_name.split(maxsplit=1)
    first_name  = splited[0]
    last_name = splited[1]
        
    user = User.objects.create_user(
		email=user_data.get("email"),
		password = user_data.get("password"),
		first_name = first_name,
		last_name = last_name
	)

    return user

def register_user(request:HttpRequest, user_data:dict):
    logging.debug("Creating the company")
    try:
        authentication_type = user_data.get("authentication_type")
        user = register_for_oauth(request, user_data) if authentication_type=="oauth" else register_for_password(request, user_data)
        return {
            "error": False,
            "content": user,
            "status": status.HTTP_200_OK
        }
    except IndexError as err:
        logging.debug(f"Index error. Invalid full name. Error: {err.args}")
        return {
            "error": True,
            "content": "Insira um nome completo",
            "status": status.HTTP_400_BAD_REQUEST
        }
    except DatabaseError as err:
        logging.debug("Internal server error. Database error.")
        return {
            "error": True,
            "content": "An internal error ocurred",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR
        }

    