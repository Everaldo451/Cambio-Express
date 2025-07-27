from django.db import transaction, IntegrityError
from users.serializers.models.user import UserSerializer
from authentication.services import JWTService
from rest_framework.test import APIRequestFactory
import pytest

@pytest.fixture
def user_data():
    return {
        "email": "valid@gmail.com",
        "password": "validPassword"
    }

@pytest.fixture
def company_data():
    return {
        "CNPJ": "02000000000001",
        "name": "Any C",
    }

@pytest.fixture
def endpoint():
    return "/api/v1/users/me/"


########USER CREATION

@pytest.fixture
def register_user(user_data):
    factory = APIRequestFactory()
    request = factory.post(
        "/api/v1/users/", 
        {
            **user_data,
        },
        format='json'
    )

    serializer = UserSerializer(
        data={**user_data},
        context={'request':request}
    )
    serializer.is_valid()
    user = serializer.save()

    jwt_service = JWTService()
    tokens = jwt_service.generate_tokens_data(request, user)

    return user, tokens

@pytest.fixture
def register_company(user_data, company_data):
    factory = APIRequestFactory()
    request = factory.post(
        "/api/v1/users/", 
        {
            **user_data
        },
        format='json'
    )

    serializer = UserSerializer(
        data={
            **user_data,
            'company': {
                **company_data
            }
        },
        context={'request':request}
    )
    serializer.is_valid()
    user = serializer.save()

    jwt_service = JWTService()
    tokens = jwt_service.generate_tokens_data(request, user)

    return user, tokens


