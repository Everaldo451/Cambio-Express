from django.http import HttpRequest, HttpResponse
from django.db import transaction, DatabaseError
from companies.models import Company
from users.models import User
from rest_framework.response import Response
from rest_framework import status
import logging

def register_company_user_exception_handler(error:Exception):
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


def create_company_user(request:HttpRequest, user_data:dict) -> Company:
    with transaction.atomic():
        user = User.objects.create_user(
            email= user_data.pop("email"), 
            password = user_data.pop("password")
        )
        company = Company(user=user, **user_data)
        company.save()
        return company


def register_company_user(request:HttpRequest, user_data:dict):
    logging.debug("Creating the company")
    try:
        company = create_company_user(request, user_data)
        return {
            "error": False,
            "message": "User with company created successfully.",
            "obj": company,
            "status": status.HTTP_201_CREATED
        }
    except Exception as error:
        return register_company_user_exception_handler(error)

    