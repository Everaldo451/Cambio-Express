import pytest

@pytest.fixture
def endpoint():
    return "/api/v1/accounts/"

@pytest.fixture
def invalid_user_data():
    return  {
        "email": "invalid@gmail.com",
        "password": "validPassword"
    }

@pytest.fixture
def access_token(login_standard_user):
    _, tokens = login_standard_user
    return tokens.get('access_token').get('value')

@pytest.mark.django_db
class TestDeposit:

    def test_success(self, client, endpoint, login_standard_user, access_token):
        user, _ = login_standard_user
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

    def test_invalid_code(self, client, endpoint, access_token):
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

    def test_account_with_code_already_exists(self, client, endpoint, access_token, create_account):
        response = client.post(endpoint,
            data={
                "code": "USD",
            },
            headers={
            "Authorization": f"Bearer {access_token}"
            }
        )
        assert response.status_code==400
        json = response.json()
        assert isinstance(json, dict)
        assert json.get('code') == ["Account with current code already exists"]