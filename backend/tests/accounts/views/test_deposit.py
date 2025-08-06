import pytest

@pytest.fixture
def endpoint():
    return '/api/v1/accounts/deposit/'

@pytest.fixture
def access_token(login_standard_user):
    _, tokens = login_standard_user
    return tokens.get('access_token').get('value')

@pytest.mark.django_db
class TestDeposit:

    def test_success(self, client, endpoint, access_token, create_account):
        account = create_account
        account_balance = account.balance
        response = client.post(endpoint+f'{account.id}/',
            data = {
                'amount': 80,
                'currency': 'EUR'
            },
            headers = {
                'Authorization': f'Bearer {access_token}'
            }
        )
        assert response.status_code == 200