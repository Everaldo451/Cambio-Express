from django.http import HttpRequest, HttpResponse
from django.db import transaction, DatabaseError
from django.contrib.auth import authenticate
from api.models import Company
from authe.form import RegisterFormForCompany
from authe.utils import generate_tokens
from authe.models import User
from rest_framework.response import Response
from rest_framework import status
from .verify_duplicate_model import verify_duplicate_model

def func(request:HttpRequest, company_form:RegisterFormForCompany) -> HttpResponse | Response:

    user_data = company_form.cleaned_data

    duplicated_user = verify_duplicate_model(request, authenticate, email = user_data.get("email"), password = user_data.get("password"))

    if duplicated_user:
        return Response({"message":"User already exists"}, status=status.HTTP_401_UNAUTHORIZED)

    duplicated_company = verify_duplicate_model(request, Company.objects.filter, CNPJ = user_data.get("CNPJ"), name = user_data.get("name"))

    if duplicated_company:
        return Response({"message":"Company already exists"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        with transaction.atomic:

            user = User.objects.create_user(email= user_data.pop("email"), password = user_data.pop("password"))

            company = Company(user = user, **user_data)

            company.save()

        return generate_tokens(request, user)

    except DatabaseError as err:

        return Response({"message":"An internal error ocurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    