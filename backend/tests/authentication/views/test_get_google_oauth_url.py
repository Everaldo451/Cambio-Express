import pytest

@pytest.fixture
def endpoint():
    return "/api/v1/auth/google/redirect/"


@pytest.mark.django_db
class TestGetGoogleOAuthURL:
    def test_success(self, client, endpoint):
        response = client.get(endpoint)
        assert response.status_code==302
