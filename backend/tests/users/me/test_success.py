import pytest

@pytest.mark.django_db
def test_company_user(client, endpoint, user_data, company_data, register_company):
    user, tokens = register_company
    access_token = tokens.get('access_token').get('value')

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