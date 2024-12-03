from django.http import HttpRequest, HttpResponse
from django.db import transaction, DatabaseError
from api.models import Company
from authe.utils import generate_tokens
from authe.models import User
from rest_framework.response import Response
from rest_framework import status

def register_company(request:HttpRequest, user_data:dict) -> HttpResponse | Response:

    try:
        with transaction.atomic:

            user = User.objects.create_user(email= user_data.pop("email"), password = user_data.pop("password"))

            company = Company(user = user, **user_data)

            company.save()

        return generate_tokens(request, user)

    except DatabaseError as err:

        return Response({"message":"An internal error ocurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    