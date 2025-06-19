from rest_framework import status
from django.db import DatabaseError
from django.db import transaction, DatabaseError

from companies.models import Company
from users.models import User
from . import Register

import logging

class CompanyUserRegister(Register[Company]):

    def register_exception_handler(self, error):
        if isinstance(error, DatabaseError):
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
        with transaction.atomic():
            user = User.objects.create_user(
                email= user_data.pop("email"), 
                password = user_data.pop("password")
            )
            company = Company(user=user, **user_data)
            company.save()
            return company
    
    
    def register_user(self, user_data):
        logging.debug("Creating the company")
        try:
            company = self.create_user(user_data)
            return {
                "error": False,
                "message": "User with company created successfully.",
                "obj": company,
                "status": status.HTTP_201_CREATED
            }
        except Exception as error:
            return self.register_exception_handler(error)
