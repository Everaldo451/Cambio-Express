import requests
import pytest

@pytest.fixture
def endpoint():
    return "/graphs/get/USD"


def test_endpoint(client, endpoint):
    response = client.get(endpoint)

    assert response.status_code == 200
    assert response.content == ""