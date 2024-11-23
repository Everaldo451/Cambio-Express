import pytest
from authe.form import LoginForm

@pytest.fixture
def login_form():
    pass


def test_login_form(login_form):

    userData = {
        "email": "valid@email.com",
        "password": "validPassword"
    }
    assert login_form(userData) == True