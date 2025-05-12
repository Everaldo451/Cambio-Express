from django.test import Client
import pytest

@pytest.fixture
def user_data():
    return  {
        "email": "valid@email.com",
        "full_name": "Any Name",
        "password": "validPassword"
    }

@pytest.fixture
def invalid_user_data():
    return  {
        "email": "invalid@gmail.com",
        "password": "validPassword"
    }

@pytest.fixture
def endpoint(main_endpoint):
    return main_endpoint+"/accounts/"

@pytest.fixture
def register_user(client:Client, main_endpoint, csrf_token, user_data):
    response = client.post(f"{main_endpoint}/users/",       
        data={
            **user_data,
            "csrfmiddlewaretoken": csrf_token
        }
    )

    assert response.status_code == 201
    assert client.cookies.get("access_token").value is not None
    
    return None