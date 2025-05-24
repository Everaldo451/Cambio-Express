from django.test import Client
from users.models import User
import pytest

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def delete_user(django_user_model, user:User):
    user.delete()

    