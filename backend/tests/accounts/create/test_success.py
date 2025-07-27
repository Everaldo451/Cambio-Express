from django.test import Client
import pytest

@pytest.mark.django_db
def test_success(client:Client, endpoint, register_user):
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

    assert response.status_code==201
    json = response.json()
    assert isinstance(json, dict)