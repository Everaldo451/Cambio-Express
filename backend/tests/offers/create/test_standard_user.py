import pytest

@pytest.mark.django_db
def test(client, endpoint, login_standard_user, offer_data):
    _, tokens = login_standard_user
    access_token = tokens.get('access_token').get('value')
    response = client.post(endpoint,
        data=offer_data,
        headers={
            'Authorization': f'Bearer {access_token}'
        }                  
    )

    assert response.status_code==403, f'Response status {response.status_code}. Error: {response.json()}'
    json = response.json()
    assert isinstance(json,dict)
