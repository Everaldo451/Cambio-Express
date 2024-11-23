import pytest
from authe.form import LoginForm

@pytest.fixture
def login_form(userData):
    pass

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


def test_login_form(valid_login_data, invalid_login_data, login_form):

    assert login_form(valid_login_data) == True