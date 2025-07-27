import pytest

@pytest.mark.django_db
def test_unauthorized(client, endpoint):
    response = client.get(endpoint)

    assert response.status_code==401, f'Response status {response.status_code}. Errors: {response.json()}'