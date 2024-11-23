from django.test import Client
from api.models import User
import pytest

@pytest.fixture
def client():
    return Client()



@pytest.fixture
def delete_user(user:User):
    user.delete()

    