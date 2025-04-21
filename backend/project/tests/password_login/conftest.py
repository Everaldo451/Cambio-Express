import pytest
from authe.form import LoginForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

@pytest.fixture
def valid_login_data():
    return  {
        "email": "valid@email.com",
        "password": "validPassword"
    }


@pytest.fixture
def invalid_login_data():
    return  {
        "email": "invalid@gmail.com",
        "password": "validPassword"
    }

@pytest.fixture
def endpoint():
    return "/auth/login/"

@pytest.fixture
def csrf_token(client):
    response = client.get("/getcsrf/")
    assert response.status_code==200
    json = response.json()
    assert isinstance(json, dict)
    return json.get("data")

@pytest.fixture
def create_user(django_user_model, valid_login_data):
    user = django_user_model.objects.create_user(**valid_login_data)
    return user
