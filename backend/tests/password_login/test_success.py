import pytest
from django.test import Client
from rest_framework.response import Response


@pytest.mark.django_db
def test_success(client:Client, endpoint, csrf_token, user_data, create_user):
    assert csrf_token is not None
    response:Response = client.post(endpoint,
        data={
            **user_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==200

    json = response.json()
    assert isinstance(json, dict)
    data:dict = json.get("data")
    assert data

    user:dict = data.get("user")
    assert user is not None
    assert user.get("company") is None

    tokens:dict = data.get("tokens")
    csrf_token = tokens.get("csrf_token")
    assert csrf_token is not None
    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    assert access_token is not None and refresh_token is not None