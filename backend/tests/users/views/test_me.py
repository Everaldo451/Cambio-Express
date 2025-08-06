import pytest

@pytest.fixture
def endpoint():
    return "/api/v1/users/me/"

@pytest.fixture
def access_token(login_company_user):
    _, tokens = login_company_user
    return tokens.get('access_token').get('value')

@pytest.fixture
def token_standard(login_standard_user):
    _, tokens = login_standard_user
    return tokens.get('access_token').get('value')

@pytest.mark.django_db
class TestMe:

    def test_company_user(self, client, endpoint, company_data, access_token):
        response = client.get(endpoint,
            headers={
                'Authorization': f'Bearer {access_token}'
            }
        )
        assert response.status_code == 200, f'Response status {response.status_code}. Errors: {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        company = json.pop('company', None)
        assert isinstance(company, dict)
        for key, value in company_data.items():
            key_company = company.get(key)
            if key_company is None:
                continue
            assert value == key_company

    def test_standard_user(self, client, endpoint, user_data, token_standard):
        response = client.get(endpoint,
            headers={
                'Authorization': f'Bearer {token_standard}'
            }
        )
        assert response.status_code == 200, f'Response status {response.status_code}. Errors: {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        company = json.pop('company', None)
        assert company is None
        for key, value in user_data.items():
            key_user = json.get(key)
            if key_user is None:
                continue
            assert value == key_user

    def test_unauthorized(self, client, endpoint, create_standard_user):
        response = client.get(
            endpoint
        )
        assert response.status_code==401, f'Response status {response.status_code}. Errors: {response.json()}'
