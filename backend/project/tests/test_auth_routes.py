import pytest
from authe.form import LoginForm

@pytest.fixture
def login_form(valid_login_data):
    return LoginForm(valid_login_data).is_valid()


@pytest.fixture
def valid_login_data():
    return  {
        "email": "valid@email.com",
        "password": "validPassword"
    }


@pytest.fixture
def invalid_login_data():
    return  {
        "password": "validPassword"
    }


def test_login_form(login_form):

    assert login_form == True