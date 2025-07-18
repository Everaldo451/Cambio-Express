from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_user_exists(client, endpoint, create_company, user_data, company_data):
    user, company = create_company
    assert user is not None and company is not None
    user_data["email"] = "other@gmail.com"
    response:Response = client.post(endpoint,
        data={
            **user_data,
            'company': {
                **company_data,
            }
        },
        content_type='application/json'
    )

    assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
    json = response.json()
    assert isinstance(json, dict)
    company_errors = json.get('company')
    assert isinstance(company_errors, dict)
    assert company_errors.get('CNPJ') is not None


@pytest.mark.django_db
def test_common_user_exists(client, endpoint, create_user, user_data):
    assert create_user is not None
    response:Response = client.post(endpoint,
        data={
            **user_data,
        },
        content_type='application/json'
    )

    assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
    json = response.json()
    assert isinstance(json, dict)
    company_errors = json.get('company')
    assert company_errors is None
    assert json.get('email') is not None