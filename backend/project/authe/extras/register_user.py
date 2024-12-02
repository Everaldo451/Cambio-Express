from django.http import HttpRequest, HttpResponse
from django.db import DatabaseError
from django.contrib.auth import authenticate
from authe.form import RegisterFormForUser
from authe.utils import generate_tokens
from authe.models import User
from rest_framework.response import Response
from rest_framework import status
from .verify_duplicate_model import verify_duplicate_model

def func(request:HttpRequest, user_form:RegisterFormForUser) -> HttpResponse | Response:

    user_data = user_form.cleaned_data

    duplicated_user = verify_duplicate_model(request, authenticate, email = user_data.get("email"), password = user_data.get("password"))

    if duplicated_user:
        return Response({"message":"User already exists"}, status=status.HTTP_401_UNAUTHORIZED)
    
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
        
        return generate_tokens(request, user)
    
    except IndexError as err:
        print(err.args)
        return Response({"Insira um nome completo"}, status=status.HTTP_400_BAD_REQUEST)
    except DatabaseError as err:
        return Response({"message":"An internal error ocurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    