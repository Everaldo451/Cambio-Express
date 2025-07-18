from rest_framework.test import APIRequestFactory

from accounts.serializers.models.account import AccountSerializer

from django.test import Client
import pytest

@pytest.fixture
def create_account(client:Client, endpoint, register_user):
    data = {
        "code": "USD",
    }
    user, tokens = register_user
    factory = APIRequestFactory()
    request = factory.post(
        endpoint, 
        {
            **data,
        },
        format='json'
    )
    request.user = user

    serializer = AccountSerializer(
        data={**data},
        context={'request':request}
    )
    serializer.is_valid()
    account = serializer.save()

@pytest.mark.django_db
def test_success(client:Client, endpoint, register_user, create_account):
    user, tokens = register_user
    access_token = tokens.get("access_token").get("value")
    response = client.post(endpoint,
        data={
            "code": "USD",
        },
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    assert json.get('code') == ["Account with current code already exists"]