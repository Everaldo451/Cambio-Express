from django.test import Client
import pytest

@pytest.fixture
def create_account(client:Client, endpoint, csrf_token):
    response = client.post(endpoint,
        data={
            "code": "USD",
            "csrfmiddlewaretoken": csrf_token
        },
    )

@pytest.mark.django_db
def test_success(client:Client, endpoint, csrf_token, register_user, create_account):
    response = client.post(endpoint,
        data={
            "code": "USD",
            "csrfmiddlewaretoken": csrf_token
        },
    )

    assert response.status_code==409
    json = response.json()
    message = json.get("message")
    assert message == "Account with current code already exists"