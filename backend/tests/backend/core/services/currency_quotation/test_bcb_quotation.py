import pytest
from backend.core.services.currency_quotation.bcb_quotation import BCBCurrencyQuotationService

@pytest.fixture
def currency_quotation():
    return BCBCurrencyQuotationService()

def test_bcb_quotation(currency_quotation):
    quotation = currency_quotation.get_current_quotation("USD", "EUR")
    assert quotation is not None
