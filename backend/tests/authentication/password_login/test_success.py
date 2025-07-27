import pytest
from django.test import Client
from rest_framework.response import Response


@pytest.mark.django_db
def test_success(client:Client, endpoint, user_data, create_standard_user):
    response:Response = client.post(endpoint,
        data={
            **user_data,
        }
    )

    assert response.status_code==200

    json = response.json()
    assert isinstance(json, dict)

    user:dict = json.get("user")
    assert user is not None
    assert user.get("company") is None

    tokens:dict = json.get("tokens")
    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    assert access_token is not None and refresh_token is not None