from django.http import HttpRequest
from django.db import DatabaseError
from users.models import User
from rest_framework import status
import logging

def register_common_user_exception_handler(error:Exception):
    if isinstance(error, IndexError):
        logging.debug(f"Index error. Invalid full name. Error: {error.args}")
        return {
            "error": True,
            "message": "Insira um nome completo",
            "status": status.HTTP_400_BAD_REQUEST
        }
    elif isinstance(error, DatabaseError):
        logging.debug("Database error.")
        return {
            "error": True,
            "message": "Database connection error.",
            "status": status.HTTP_502_BAD_GATEWAY
        }
    return {
        "error": True,
        "message": "Internal server error.",
        "status": status.HTTP_500_INTERNAL_SERVER_ERROR
    }


def create_user(request:HttpRequest, user_data:dict) -> User:
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


def register_common_user(request:HttpRequest, user_data:dict):
    logging.debug("Creating the user")
    try:
        user = create_user(request, user_data)
        return {
            "error": False,
            "message": "User created successfully.",
            "obj": user,
            "status": status.HTTP_201_CREATED
        }
    except Exception as error:
        return register_common_user_exception_handler(error)


    