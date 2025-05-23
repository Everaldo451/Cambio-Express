import pytest

@pytest.mark.django_db
def test_success(client, endpoint):
    response = client.get(endpoint)

    assert response.status_code==302
