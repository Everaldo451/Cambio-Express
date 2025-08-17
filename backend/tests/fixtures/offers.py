import pytest
from rest_framework.test import APIRequestFactory

from offers.serializers.models import InvestmentOfferSerializer

@pytest.fixture
def offer_data():
    return {
        'min_value': '100.00',
        'monetary_index': 'SELIC',
        'percent': '95.55'
    }

@pytest.fixture
def create_offer(login_company_user, offer_data):
    user, _ = login_company_user
    factory = APIRequestFactory()
    request = factory.post(
        '',
        data={**offer_data},
    )
    request.user = user

    serializer = InvestmentOfferSerializer(
        data={**offer_data}, 
        context={'request':request}
    )
    serializer.is_valid()
    return serializer.save()

