from django.test import Client
from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_user_bad_request(client:Client, endpoint, user_data, company_data):
    company_data.pop("name")
    response:Response = client.post(endpoint,
        data={
            **user_data,
            'company': {
                **company_data
            }
        },
        content_type="application/json"
    )

    assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
    json = response.json()
    assert isinstance(json, dict)
    company_errors = json.get('company')
    assert isinstance(company_errors, dict)
    assert company_errors.get('name')


@pytest.mark.django_db
def test_common_user_bad_request(client:Client, endpoint, user_data):
    user_data.pop("email")
    response:Response = client.post(endpoint,
        data={
            **user_data,
        },
        content_type="application/json"
    )

    assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
    json = response.json()
    assert isinstance(json, dict)
    company_errors = json.get('company')
    assert not company_errors
    assert json.get('email') is not None

