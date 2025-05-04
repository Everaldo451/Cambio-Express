import pytest
from rest_framework.response import Response

@pytest.mark.django_db
def test_bad_request(client, endpoint, csrf_token, invalid_user_data, create_user):
    assert csrf_token is not None
    invalid_user_data.pop("password")
    response:Response = client.post(endpoint,
        data={
            **invalid_user_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="Invalid credentials"