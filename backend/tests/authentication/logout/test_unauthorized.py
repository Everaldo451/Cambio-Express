import pytest

@pytest.mark.django_db
def test_unauthorized(client, endpoint):
    response = client.post(endpoint)

    assert response.status_code==400, f'Response status {response.status_code}. Errors: {response.json()}'
    json = response.json()
    assert isinstance(json, dict)
    refresh_error = json.get('refresh')
    assert refresh_error is not None