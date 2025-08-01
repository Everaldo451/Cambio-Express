from django.test import Client
import pytest

@pytest.mark.django_db
def test_success(client:Client, endpoint, login_standard_user):
    user, tokens = login_standard_user
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
    user_in_response = json.pop('user', None)
    assert user_in_response == user.email