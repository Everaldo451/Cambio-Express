from django.test import Client
from api.models import User
import pytest

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def csrf_token(client):
    response = client.get("/getcsrf/")
    assert response.status_code==200
    json = response.json()
    assert isinstance(json, dict)
    return json.get("data")

@pytest.fixture
def delete_user(django_user_model ,user:User):
    user.delete()

    