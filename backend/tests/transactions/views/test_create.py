import pytest

@pytest.fixture
def modify_user_data(user_data):
    user_data['email'] = 'otheremail@gmail.com'

@pytest.fixture
def endpoint():
    return '/api/v1/transactions/'

@pytest.mark.django_db
class TestCreate:
    def test_success(
            self,
            client, 
            endpoint, 
            create_offer, 
            modify_user_data,
            login_standard_user, 
            create_account,
            transaction_data
        ):
        _, tokens = login_standard_user
        access_token = tokens.get('access_token').get('value')
        response = client.post(endpoint,
            headers={
                'Authorization': f'Bearer {access_token}'
            },
            data={
                **transaction_data,
                'investment_offer': create_offer.id
            },
            content_type='application/json'
        )
        assert response.status_code == 201, f'Response status {response.status_code}. Error: {response.json()}'