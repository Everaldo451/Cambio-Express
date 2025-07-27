from rest_framework.test import APIRequestFactory

from users.serializers.models.user import UserSerializer
import pytest

@pytest.fixture
def user_data():
    return  {
        "email": "valid@email.com",
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
    return "/api/v1/auth/login/"

@pytest.fixture
def create_user(django_user_model, endpoint, user_data):
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
    return serializer.save()
