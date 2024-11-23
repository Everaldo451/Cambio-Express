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
def login_form(valid_login_data):
    form = LoginForm(valid_login_data)
    return form.is_valid()


@pytest.fixture
def auth(invalid_login_data):
    user = authenticate(None, **invalid_login_data)
    return user, user is not None


@pytest.fixture
def create_user(django_user_model, invalid_login_data):
    user = django_user_model.objects.create_user(**invalid_login_data)
    return user



@pytest.mark.django_db
def test_login_form(create_user, login_form, auth):

    assert login_form
    user, isNoNone = auth
    assert isNoNone
    assert user == create_user




