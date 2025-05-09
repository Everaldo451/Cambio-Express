from django.test import Client
import pytest

@pytest.mark.django_db
def test_success(client:Client, endpoint, csrf_token, register_user):
    response = client.post(endpoint,
        data={
            "code": "USD",
            "csrfmiddlewaretoken": csrf_token
        },
    )

    assert response.status_code==201
    json = response.json()
    message = json.get("message")
    assert message == "Account created successful."