from django.test import Client
from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_bad_request(client:Client, endpoint, csrf_token, user_data, company_data):
    assert csrf_token is not None
    company_data.pop("name")
    response:Response = client.post(endpoint,
        data={
            **user_data,
            **company_data,
            "is_company": True,
            "csrfmiddlewaretoken": csrf_token
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
def test_user_bad_request(client:Client, endpoint, csrf_token, user_data):
    assert csrf_token is not None
    user_data.pop("full_name")
    response:Response = client.post(endpoint,
        data={
            **user_data,
            "is_company": False,
            "csrfmiddlewaretoken": csrf_token
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
