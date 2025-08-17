import pytest
from rest_framework.test import APIRequestFactory

from accounts.serializers.models import AccountSerializer

@pytest.fixture
def account_data():
    return {
        'currency': 'USD',
    }

@pytest.fixture
def other_account_data():
    return {
        'currency': 'EUR',
    }

@pytest.fixture
def create_account(login_standard_user, account_data):
    user, _ = login_standard_user
    factory = APIRequestFactory()
    request = factory.post(
        '',
        data={**account_data},
    )
    request.user = user

    serializer =  AccountSerializer(
        data={**account_data}, 
        context={'request':request}
    )
    serializer.is_valid()
    account = serializer.save()
    account.balance+=100
    account.save()
    return account

@pytest.fixture
def create_other_account(login_standard_user, other_account_data):
    user, _ = login_standard_user
    factory = APIRequestFactory()
    request = factory.post(
        '',
        data={**other_account_data},
    )
    request.user = user

    serializer =  AccountSerializer(
        data={**other_account_data}, 
        context={'request':request}
    )
    serializer.is_valid()
    account = serializer.save()
    account.balance+=100
    account.save()
    return account

