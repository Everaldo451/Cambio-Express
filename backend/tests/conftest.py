from django.test import Client

from .fixtures.user import (
    user_data, company_data, client_data,
    create_standard_user, 
    login_standard_user, 
    create_company_user, 
    login_company_user
)
from .fixtures.offers import (
    offer_data,
    create_offer
)
from .fixtures.transactions import (
    transaction_data
)
from .fixtures.accounts import (
    account_data,
    other_account_data,
    create_account,
    create_other_account
)

import pytest

@pytest.fixture
def client():
    return Client()
    