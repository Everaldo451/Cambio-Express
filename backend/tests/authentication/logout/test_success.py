import pytest

@pytest.mark.django_db
def test_success(client, endpoint, login_standard_user):
    _, tokens = login_standard_user
    access_token = tokens.get('access_token').get('value')
    refresh_token = tokens.get('refresh_token').get('value')

    response = client.post(endpoint,
        data={
            "refresh": refresh_token
        },
    )

    assert response.status_code==200, f'Response status {response.status_code}. Errors: {response.json()}'