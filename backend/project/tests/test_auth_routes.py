import pytest
from authe.form import LoginForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework.response import Response

@pytest.fixture
def valid_login_data():
    return  {
        "email": "valid@email.com",
        "password": "validPassword"
    }


@pytest.fixture
def invalid_login_data():
    return  {
        "email": "valid@gmail.com",
        "password": ""
    }


@pytest.fixture
def login_form(valid_login_data):
    form = LoginForm(valid_login_data)
    return form.is_valid()


@pytest.fixture
def auth(valid_login_data):
    user = authenticate(None, **valid_login_data)
    return user, user is not None


@pytest.fixture
def create_user(django_user_model, valid_login_data):
    user = django_user_model.objects.create_user(**valid_login_data)
    return user


@pytest.fixture
def response(django_user_model, auth):
    resp = Response({
        "access": "oi",
        "refresh": "ola"
    })

    resp.set_cookie("access_token", "oi")
    resp.set_cookie("refresh_token", "ola")
    return resp


@pytest.mark.django_db
def test_login_form(create_user, login_form, auth, response):

    assert login_form
    user, isNoNone = auth
    assert isNoNone
    assert user == create_user

@pytest.mark.django_db
def test_login_response(response):
    
    assert isinstance(response, Response)
    assert isinstance(response.data, dict)
    assert response.data.get("access")
    assert response.data.get("refresh")
    assert response.cookies.get("access_token")
    assert response.cookies.get("refresh_token")




