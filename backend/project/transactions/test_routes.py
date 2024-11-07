from django.test import TestCase, Client
import pytest

@pytest.fixture
def client():
    return Client()


def test_get_route(client:Client):
    response = client.get("/tran/getmany/USD/IPCA")
    assert response.status_code == 200

# Create your tests here.
