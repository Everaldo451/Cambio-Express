from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_success(client, endpoint, csrf_token, user_data, company_data):
    assert csrf_token is not None
    response:Response = client.post(endpoint,
        data={
            **user_data,
            **company_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==200
    json = response.json()
    assert isinstance(json, dict)
    csrf_token = json.get("csrf_token")
    assert csrf_token is not None
    access_token = response.cookies.get("access_token")
    refresh_token = response.cookies.get("refresh_token")
    assert access_token is not None and refresh_token is not None


@pytest.mark.django_db
def test_user_success(client, endpoint, csrf_token, user_data):
    assert csrf_token is not None
    response:Response = client.post(endpoint,
        data={
            **user_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code==200
    json = response.json()
    assert isinstance(json, dict)
    csrf_token = json.get("csrf_token")
    assert csrf_token is not None
    access_token = response.cookies.get("access_token")
    refresh_token = response.cookies.get("refresh_token")
    assert access_token is not None and refresh_token is not None