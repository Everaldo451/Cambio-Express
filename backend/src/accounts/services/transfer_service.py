from backend.core.services.currency_quotation.base import CurrencyQuotationService
from accounts.models import Account

class TransferService:
    
    def __init__(self, currency_quotation_service:CurrencyQuotationService):
        self.quotation_service = currency_quotation_service

    def transfer_from_internal_account(self, from_account:Account, to_account:Account, amount):
        converted_ammount = None
        if from_account.code == to_account.code:
            converted_ammount = amount
        else:
            quotation = self.quotation_service.get_current_quotation(
                from_account.code, to_account.code
            )
            converted_ammount = amount/quotation

        if amount > from_account.balance:
            raise ValueError("Insufficient balance.")

        from_account.balance -= amount
        to_account.balance += converted_ammount

        from_account.save()
        to_account.save()


    
        