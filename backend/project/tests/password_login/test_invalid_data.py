import pytest
from rest_framework.response import Response

@pytest.mark.django_db
def test_invalid_data(client, endpoint, csrf_token, invalid_login_data, create_user):
    assert csrf_token is not None
    response:Response = client.post(endpoint,
        data={
            **invalid_login_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==401
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="User don't exists"