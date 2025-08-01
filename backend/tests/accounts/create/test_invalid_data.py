from django.test import Client
import pytest

@pytest.mark.django_db
class TestInvalidData:

    def test_invalid_code(self, client:Client, endpoint, login_standard_user):
        _, tokens = login_standard_user
        access_token = tokens.get("access_token").get("value")
        response = client.post(endpoint,
            data={
                "code": "A",
            },
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

        assert response.status_code==400
        json = response.json()
        assert isinstance(json, dict)
        assert json.get('code') is not None
        assert json.get('user') is None