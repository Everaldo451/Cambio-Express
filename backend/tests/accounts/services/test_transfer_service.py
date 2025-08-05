import pytest
from accounts.services.transfer_service import TransferService
from backend.core.services.currency_quotation.bcb_quotation import BCBCurrencyQuotationService


@pytest.fixture
def transfer_service():
    return TransferService(BCBCurrencyQuotationService())

@pytest.mark.django_db
def test_transfer_from_external_account(transfer_service, create_account):
    account = create_account
    balance = account.balance
    transfer_service.transfer_from_external_account(account, 'EUR', 100)

    assert balance < account.balance

@pytest.mark.django_db
class TestTransferFromInternalAccount:

    def test_success_case(
            self, 
            transfer_service, 
            create_account, 
            create_other_account
        ):
        from_account = create_account
        to_account = create_other_account
        from_account_balance = from_account.balance
        to_account_balance = to_account.balance

        transfer_service.transfer_from_internal_account(from_account, to_account, 80)

        assert from_account_balance > from_account.balance
        assert to_account_balance < to_account.balance

    def test_insufficient_balance(
            self, 
            transfer_service, 
            create_account, 
            create_other_account
        ):
        from_account = create_account
        to_account = create_other_account
        from_account_balance = from_account.balance
        to_account_balance = to_account.balance

        with pytest.raises(ValueError) as error:
            transfer_service.transfer_from_internal_account(from_account, to_account, 120)

        assert error.errisinstance(ValueError)
        assert str(error.value) == 'Insufficient balance.'

