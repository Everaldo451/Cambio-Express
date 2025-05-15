from django.test import Client
from companies.models import Company

from rest_framework_simplejwt.tokens import RefreshToken
import pytest

@pytest.fixture
def company_model():
    return Company

@pytest.fixture
def user_data():
    return {
        "email": "valid@gmail.com",
        "full_name": "Any Name",
        "password": "validPassword"
    }

@pytest.fixture
def other_user_data():
    return {
        "email": "other@gmail.com",
        "full_name": "Any Name",
        "password": "validPassword"
    }

@pytest.fixture
def company_data():
    return {
        "CNPJ": "0200000001",
        "name": "Any C",
    }

@pytest.fixture
def endpoint(main_endpoint):
    return main_endpoint+"/me/"


########USER CREATION

@pytest.fixture()
def register_user(django_user_model, user_data):
    user=None
    try:
        user = django_user_model.objects.create_user(
            email=user_data.get("email"),
            password=user_data.get("password")
        )
        refresh_token = RefreshToken.for_user(user)
        return {
            "access_token": {
                "lifetime": refresh_token.access_token.lifetime,
                "value": str(refresh_token.access_token),
            },
            "refresh_token": {
                "lifetime": refresh_token.lifetime,
                "value": str(refresh_token),
            },
        }
    except:
        return None




@pytest.fixture
def create_other_user(django_user_model, other_user_data):
    try:
        user = django_user_model.objects.create_user(
            email=other_user_data.get("email"),
            password=other_user_data.get("password")
        )
        return user
    
    except: return None


@pytest.fixture
def splited_name(user_data):
    full_name = user_data.get("full_name")

    try:
        splited = full_name.split(maxsplit=1)
        first_name  = splited[0]
        last_name = splited[1]
        return first_name, last_name
    except IndexError:
        return None

