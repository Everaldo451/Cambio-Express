import pytest

@pytest.mark.django_db
def test_success(client, endpoint):
    response = client.get(endpoint)

    assert response.status_code==200
    json = response.json()
    assert isinstance(json, dict)
    url = json.get("url")
    assert not isinstance(url, str)
