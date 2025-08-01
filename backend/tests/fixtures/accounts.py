import pytest
from rest_framework.test import APIRequestFactory

from accounts.serializers.models import AccountSerializer

@pytest.fixture
def account_data():
    return {
        'code': 'USD',
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
    return serializer.save()

