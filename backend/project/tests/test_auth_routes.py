import pytest
from authe.form import LoginForm
from django.contrib.auth import authenticate

@pytest.fixture
def valid_login_data():
    return  {
        "email": "valid@email.com",
        "password": "validPassword"
    }


@pytest.fixture
def invalid_login_data():
    return  {
        "email": "",
        "password": "validPassword"
    }

@pytest.fixture
def login_form(invalid_login_data):
    return LoginForm(invalid_login_data).is_valid()


@pytest.mark.django_db
def test_login_form(login_form, auth):

    assert login_form == False
    assert auth == False




