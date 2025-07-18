from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.services import JWTService

from users.serializers.models.user import UserSerializer

from django.test import Client
import pytest

@pytest.fixture
def user_data():
    return  {
        "email": "valid@email.com",
        "full_name": "Any Name",
        "password": "validPassword"
    }

@pytest.fixture
def invalid_user_data():
    return  {
        "email": "invalid@gmail.com",
        "password": "validPassword"
    }

@pytest.fixture
def endpoint():
    return "/api/v1/accounts/"

@pytest.fixture
def register_user(client:Client, user_data):
    factory = APIRequestFactory()
    request = factory.post(
        endpoint, 
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