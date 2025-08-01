import pytest

@pytest.mark.django_db
class TestInvalidData:

    def test_invalid_code(
            self, 
            client, 
            endpoint, 
            login_company_user, 
            offer_data
        ):
        _, tokens = login_company_user
        access_token = tokens.get('access_token').get('value')
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
            login_company_user, 
            offer_data
        ):
        _, tokens = login_company_user
        access_token = tokens.get('access_token').get('value')
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
            login_company_user, 
            offer_data
        ):
        _, tokens = login_company_user
        access_token = tokens.get('access_token').get('value')
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
            login_company_user, 
            offer_data
        ):
        _, tokens = login_company_user
        access_token = tokens.get('access_token').get('value')
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