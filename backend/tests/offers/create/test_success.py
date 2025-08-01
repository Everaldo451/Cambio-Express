import pytest

@pytest.mark.django_db
def test_success(client, endpoint, login_company_user, offer_data):
    user, tokens = login_company_user
    access_token = tokens.get("access_token").get("value")
    response = client.post(endpoint,
        data=offer_data,
        headers={
            'Authorization': f'Bearer {access_token}'
        }
    )

    assert response.status_code == 201, f'Response status {response.status_code}. Error: {response.json()}'
    json = response.json()
    assert isinstance(json, dict)
    created_by = json.pop('created_by', None)
    assert created_by is not None
    for key, value in offer_data.items():
        response_key = json[key]
        if response_key:
            assert response_key == value, f'Value in json: {response_key}. Value in data: {value}'
