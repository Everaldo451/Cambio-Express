from rest_framework.response import Response
import pytest

@pytest.mark.django_db
def test_company_user_success(client, endpoint, user_data, company_data):
    response:Response = client.post(endpoint,
        data={
            **user_data,
            'company': {
                **company_data
            }
        },
        content_type='application/json'
    )

    assert response.status_code==201, f'Error status {response.status_code} - {response.json()}'

    json = response.json()
    assert isinstance(json, dict)
    for key, value in json.items():
        value2 = user_data.get(key)
        if value2:
            assert value2 == value


@pytest.mark.django_db
def test_common_user_success(client, endpoint, user_data):
    response:Response = client.post(endpoint,
        data={**user_data},
        content_type='application/json'
    )

    assert response.status_code == 201, f'Error status {response.status_code} - {response.json()}'
    
    json = response.json()
    assert isinstance(json, dict)
    for key, value in json.items():
        value2 = user_data.get(key)
        if value2:
            assert value2 == value