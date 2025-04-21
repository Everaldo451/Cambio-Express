import pytest
from rest_framework.response import Response


@pytest.mark.django_db
def test_success(client, endpoint, csrf_token, valid_login_data, create_user):
    assert csrf_token is not None
    response:Response = client.post(endpoint,
        data={
            **valid_login_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==200
    json = response.json()
    assert isinstance(json, dict)
    data = json.get("data")
    assert isinstance(data, dict)
    access_token = data.get("access_token")
    refresh_token = data.get("refresh_token")
    assert access_token is not None and refresh_token is not None