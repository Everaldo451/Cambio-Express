import pytest

@pytest.fixture
def endpoint():
    return '/api/v1/offers/'

@pytest.fixture
def access_token(login_company_user):
    _, tokens = login_company_user
    return tokens.get('access_token').get('value')

@pytest.fixture
def token_standard(login_standard_user):
    _, tokens = login_standard_user
    return tokens.get('access_token').get('value')

@pytest.mark.django_db
class TestCreate:

    def test_success(self, client, endpoint, access_token, offer_data):
        response = client.post(endpoint,
            data=offer_data,
            headers={
                'Authorization': f'Bearer {access_token}'
            }
        )
        assert response.status_code == 201, f'Response status {response.status_code}. Error: {response.json()}'
        json = response.json()
        assert isinstance(json, dict)
        created_by = json.pop('created_by', None)
        assert created_by is not None
        for key, value in offer_data.items():
            response_key = json[key]
            if response_key:
                assert response_key == value, f'Value in json: {response_key}. Value in data: {value}'

    def test_is_standard_user(self, client, endpoint, token_standard, offer_data):
        response = client.post(endpoint,
            data=offer_data,
            headers={
                'Authorization': f'Bearer {token_standard}'
            }                  
        )
        assert response.status_code==403, f'Response status {response.status_code}. Error: {response.json()}'
        json = response.json()
        assert isinstance(json,dict)

    def test_invalid_code(
            self, 
            client, 
            endpoint, 
            access_token, 
            offer_data
        ):
        offer_data['code'] = 'CODE'
        response = client.post(endpoint,
            data=offer_data,
            headers={
                'Authorization': f'Bearer {access_token}'
            }                  
        )
        assert response.status_code==400, f'Response status {response.status_code}. Error: {response.json()}'
        json = response.json()
        assert isinstance(json,dict)
        code_error = json.pop('code', None)
        assert code_error is not None

    def test_invalid_index_variable(
            self, 
            client, 
            endpoint, 
            access_token, 
            offer_data
        ):
        offer_data['index_variable'] = 'ANOTHERVAR'
        response = client.post(endpoint,
            data=offer_data,
            headers={
                'Authorization': f'Bearer {access_token}'
            }                  
        )
        assert response.status_code==400, f'Response status {response.status_code}. Error: {response.json()}'
        json = response.json()
        assert isinstance(json,dict)
        index_variable_error = json.pop('index_variable', None)
        assert index_variable_error is not None

    def test_negative_min_value(
            self, 
            client, 
            endpoint, 
            access_token, 
            offer_data
        ):
        offer_data['min_value'] = '-90.00'
        response = client.post(endpoint,
            data=offer_data,
            headers={
                'Authorization': f'Bearer {access_token}'
            }                  
        )
        assert response.status_code==400, f'Response status {response.status_code}. Error: {response.json()}'
        json = response.json()
        assert isinstance(json,dict)
        min_value_error = json.pop('min_value', None)
        assert min_value_error is not None

    def test_negative_percent(
            self, 
            client, 
            endpoint, 
            access_token, 
            offer_data
        ):
        offer_data['percent'] = '-90.00'
        response = client.post(endpoint,
            data=offer_data,
            headers={
                'Authorization': f'Bearer {access_token}'
            }                  
        )
        assert response.status_code==400, f'Response status {response.status_code}. Error: {response.json()}'
        json = response.json()
        assert isinstance(json,dict)
        percent_error = json.pop('percent', None)
        assert percent_error is not None
