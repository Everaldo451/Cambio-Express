import pytest

@pytest.fixture
def invalid_user_data():
    return  {
        "email": "invalid@gmail.com",
        "password": "validPassword"
    }

@pytest.fixture
def endpoint():
    return "/api/v1/auth/login/"

@pytest.mark.django_db
class TestPasswordLogin:

    def test_success(self, client, endpoint, user_data, create_standard_user):
        response = client.post(endpoint,
            data={
                **user_data,
            }
        )
        assert response.status_code==200
        json = response.json()
        assert isinstance(json, dict)
        user:dict = json.get("user")
        assert user is not None
        assert user.get("company") is None
        tokens:dict = json.get("tokens")
        access_token = tokens.get("access_token")
        refresh_token = tokens.get("refresh_token")
        assert access_token is not None and refresh_token is not None

    def test_invalid_user(self, client, endpoint, invalid_user_data, create_standard_user):
        response = client.post(endpoint,
            data={
                **invalid_user_data,
            }
        )
        assert response.status_code==400
        json = response.json()
        assert isinstance(json, dict)
        assert json.get('non_field_errors') is not None

    def test_bad_request(self, client, endpoint, user_data, create_standard_user):
        user_data.pop("password")
        response = client.post(endpoint,
            data={
                **user_data,
            }
        )
        assert response.status_code==400
        json = response.json()
        assert isinstance(json, dict)
        assert json.get('password') is not None