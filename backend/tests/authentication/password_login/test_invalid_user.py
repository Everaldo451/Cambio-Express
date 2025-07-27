import pytest
from rest_framework.response import Response

@pytest.mark.django_db
def test_invalid_user(client, endpoint, invalid_user_data, create_user):
    response:Response = client.post(endpoint,
        data={
            **invalid_user_data,
        }
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    assert json.get('non_field_errors') is not None