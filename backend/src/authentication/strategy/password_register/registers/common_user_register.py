from rest_framework import status
from django.db import DatabaseError

from users.models import User
from . import Register

import logging

class CommonUserRegister(Register[User]):

    def register_exception_handler(self, error):
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

    def create_user(self, user_data):
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
    
    
    def register_user(self, user_data):
        logging.debug("Creating the user")
        try:
            user = self.create_user(user_data)
            return {
                "error": False,
                "message": "User created successfully.",
                "obj": user,
                "status": status.HTTP_201_CREATED
            }
        except Exception as error:
            return self.register_exception_handler(error)
