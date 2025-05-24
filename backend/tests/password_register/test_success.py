from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_user_success(client, endpoint, user_data, company_data):
    response:Response = client.post(endpoint,
        data={
            **user_data,
            **company_data,
            "is_company": True,
        },
    )

    assert response.status_code==201

    json = response.json()
    assert isinstance(json, dict)
    data:dict = json.get("data")
    assert data

    user:dict = data.get("user")
    assert user is not None
    assert user.get("company") is not None

    tokens:dict = data.get("tokens")
    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    assert access_token is not None and refresh_token is not None


@pytest.mark.django_db
def test_common_user_success(client, endpoint, user_data):
    response:Response = client.post(endpoint,
        data={
            **user_data,
            "is_company": False,
        },
    )

    assert response.status_code == 201
    
    json = response.json()
    assert isinstance(json, dict)
    data:dict = json.get("data")
    assert data

    user:dict = data.get("user")
    assert user is not None
    assert user.get("company") is None

    tokens:dict = data.get("tokens")
    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    assert access_token is not None and refresh_token is not None