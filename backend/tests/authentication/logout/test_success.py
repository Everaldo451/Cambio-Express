import pytest

@pytest.mark.django_db
def test_success(client, endpoint, login_standard_user):
    user, tokens = login_standard_user
    access_token = tokens.get('access_token').get('value')

    response = client.get(endpoint,
        headers={
            'Authorization': f'Bearer {access_token}'
        }
    )

    assert response.status_code==204, f'Response status {response.status_code}. Errors: {response.json()}'