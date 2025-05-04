from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_bad_request(client, endpoint, csrf_token, user_data, company_data):
    assert csrf_token is not None
    company_data.pop("name")
    response:Response = client.post(endpoint,
        data={
            **user_data,
            **company_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="Invalid company credentials."


@pytest.mark.django_db
def test_user_bad_request(client, endpoint, csrf_token, user_data):
    assert csrf_token is not None
    user_data.pop("full_name")
    response:Response = client.post(endpoint,
        data={
            **user_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==400
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="Invalid user credentials."