import pytest

@pytest.fixture
def endpoint():
    return '/api/v1/auth/logout/'

@pytest.fixture
def refresh_token(login_standard_user):
    _, tokens = login_standard_user
    return tokens.get('refresh_token').get('value')

@pytest.mark.django_db
class TestLogout:

    def test_success(self, client, endpoint, refresh_token):
        response = client.post(endpoint,
            data={
                "refresh": refresh_token
            },
        )
        assert response.status_code==200, f'Response status {response.status_code}. Errors: {response.json()}'

    def test_token_field_is_empty(self, client, endpoint):
        response = client.post(endpoint)
        assert response.status_code==400, f'Response status {response.status_code}. Errors: {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        refresh_error = json.get('refresh')
        assert refresh_error is not None