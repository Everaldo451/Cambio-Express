from django.http import HttpRequest, HttpResponse
from django.db import transaction, DatabaseError
from api.models import Company
from api.models import User
from rest_framework.response import Response
from rest_framework import status

from .generate_jwt_response import generate_full_jwt_response
import logging

def register_company(request:HttpRequest, user_data:dict) -> HttpResponse | Response:

    logging.debug("Creating the company")
    try:
        with transaction.atomic():
            user = User.objects.create_user(email= user_data.pop("email"), password = user_data.pop("password"))
            company = Company(user = user, **user_data)
            company.save()
        return generate_full_jwt_response(request, user, status.HTTP_201_CREATED)
    except DatabaseError as err:
        logging.debug("Internal server error. Database error.")
        return Response({"message":"An internal error ocurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    