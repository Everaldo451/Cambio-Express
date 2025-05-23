from django.test import Client
import pytest

@pytest.fixture
def create_account(client:Client, endpoint, csrf_token, register_user):
    tokens:dict = register_user
    access_token = tokens.get("access_token").get("value")
    response = client.post(endpoint,
        data={
            "code": "USD",
            "csrfmiddlewaretoken": tokens.get("csrf_token"),
        },
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

@pytest.mark.django_db
def test_success(client:Client, endpoint, csrf_token, register_user, create_account):
    tokens:dict = register_user
    access_token = tokens.get("access_token").get("value")
    response = client.post(endpoint,
        data={
            "code": "USD",
            "csrfmiddlewaretoken": tokens.get("csrf_token"),
        },
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code==409
    json = response.json()
    message = json.get("message")
    assert message == "Account with current code already exists"