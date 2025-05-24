from django.test import Client
from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_user_bad_request(client:Client, endpoint, user_data, company_data):
    company_data.pop("name")
    response:Response = client.post(endpoint,
        data={
            **user_data,
            **company_data,
            "is_company": True,
        },
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="Invalid credentials."
    errors:dict = json.get("errors")
    error = errors.get("non_field_errors")
    assert error[0] == "Company fields are required"


@pytest.mark.django_db
def test_common_user_bad_request(client:Client, endpoint, user_data):
    user_data.pop("full_name")
    response:Response = client.post(endpoint,
        data={
            **user_data,
            "is_company": False,
        },
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="Invalid credentials."
    errors:dict = json.get("errors")
    error = errors.get("non_field_errors")
    assert error[0] == "User fields are required"
