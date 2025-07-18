import pytest
from rest_framework.response import Response

@pytest.mark.django_db
def test_bad_request(client, endpoint, invalid_user_data, create_user):
    invalid_user_data.pop("password")
    response:Response = client.post(endpoint,
        data={
            **invalid_user_data,
        }
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    assert json.get('password') is not None