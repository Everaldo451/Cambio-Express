import pytest

@pytest.fixture
def endpoint():
    return "/api/v1/users/"

@pytest.mark.django_db
class TestCreate:

    def test_company_user_success(self, client, endpoint, user_data, company_data):
        response = client.post(endpoint,
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

    def test_standard_user_success(self, client, endpoint, user_data, client_data):
        response = client.post(endpoint,
            data={
                **user_data,
                'client': {**client_data}
            },
            content_type='application/json'
        )
        assert response.status_code == 201, f'Error status {response.status_code} - {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        for key, value in json.items():
            value2 = user_data.get(key)
            if value2:
                assert value2 == value

    def test_user_without_type(self, client, endpoint, user_data):
        response = client.post(endpoint,
            data={
                **user_data,
            },
            content_type='application/json'
        )
        assert response.status_code==400, f'Response status {response.status_code} - {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        user_type_error = json.get('user_type')
        assert user_type_error is not None

    def test_company_user_without_name(self, client, endpoint, user_data, company_data):
        company_data.pop("name")
        response = client.post(endpoint,
            data={
                **user_data,
                'company': {
                    **company_data
                }
            },
            content_type="application/json"
        )
        assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        company_errors = json.get('company')
        assert isinstance(company_errors, dict)
        assert company_errors.get('name')

    def test_standard_user_without_email(self, client, endpoint, user_data, client_data):
        user_data.pop("email")
        response = client.post(endpoint,
            data={
                **user_data,
                'client': {**client_data}
            },
            content_type="application/json"
        )
        assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        company_errors = json.get('company')
        assert not company_errors
        assert json.get('email') is not None

    def test_company_user_already_exists(
            self, client, endpoint, create_company_user, user_data, company_data
        ):
        user, company = create_company_user
        assert user is not None and company is not None
        user_data["email"] = "other@gmail.com"
        response = client.post(endpoint,
            data={
                **user_data,
                'company': {
                    **company_data,
                }
            },
            content_type='application/json'
        )
        assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        company_errors = json.get('company')
        assert isinstance(company_errors, dict)
        assert company_errors.get('CNPJ') is not None

    def test_standard_user_already_exists(
            self, client, endpoint, create_standard_user, user_data, client_data
        ):
        user, user_client = create_standard_user
        assert user is not None and user_client is not None
        response = client.post(endpoint,
            data={
                **user_data,
                'client': {**client_data}
            },
            content_type='application/json'
        )
        assert response.status_code==400, f'Error status {response.status_code} - {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        company_errors = json.get('company')
        assert company_errors is None
        assert json.get('email') is not None