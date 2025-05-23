import pytest

@pytest.fixture
def user_data():
    return  {
        "email": "valid@email.com",
        "password": "validPassword"
    }

@pytest.fixture
def invalid_user_data():
    return  {
        "email": "invalid@gmail.com",
        "password": "validPassword"
    }

@pytest.fixture
def endpoint():
    return "/auth/login/"

@pytest.fixture
def create_user(django_user_model, user_data):
    user = django_user_model.objects.create_user(**user_data)
    return user
