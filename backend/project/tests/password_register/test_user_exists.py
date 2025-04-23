from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_exists(client, endpoint, csrf_token, create_company, user_data, company_data):
    user, company = create_company
    assert user is not None and company is not None
    assert csrf_token is not None
    user_data["email"] = "other@gmail.com"
    company_data["is_company"] = "on"
    response:Response = client.post(endpoint,
        data={
            **user_data,
            **company_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==401
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="Company already exists."


@pytest.mark.django_db
def test_user_exists(client, endpoint, csrf_token, create_user, user_data):
    assert create_user is not None
    assert csrf_token is not None
    response:Response = client.post(endpoint,
        data={
            **user_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==401
    json = response.json()
    assert isinstance(json, dict)
    message = json.get("message")
    assert message=="User already exists."