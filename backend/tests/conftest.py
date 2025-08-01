from django.test import Client
from rest_framework.test import APIRequestFactory

from users.serializers.models.user import UserSerializer
from authentication.services import JWTService

from .fixtures.user import (
    user_data, company_data, 
    create_standard_user, 
    login_standard_user, 
    create_company_user, 
    login_company_user
)

from .fixtures.offers import (
    offer_data
)

import pytest

@pytest.fixture
def client():
    return Client()



"""
@pytest.fixture
def user_data():
    return {
        "email": "valid@gmail.com",
        "first_name": "Any",
        "last_name": "Name",
        "password": "validPassword"
    }

@pytest.fixture
def company_data():
    return {
        "CNPJ": "02000000000001",
        "name": "Any C",
    }

@pytest.fixture
def create_standard_user(user_data):
    factory = APIRequestFactory()
    request = factory.post(
        '', 
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

@pytest.fixture
def register_standard_user(user_data, create_standard_user):
    factory = APIRequestFactory()
    request = factory.post(
        '', 
        {
            **user_data,
        },
        format='json'
    )
    jwt_service = JWTService()
    tokens = jwt_service.generate_tokens_data(request, create_standard_user)

    return create_standard_user, tokens

@pytest.fixture
def create_company_user(user_data):
    factory = APIRequestFactory()
    request = factory.post(
        '', 
        {**user_data},
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
    return user, user.company
"""
    