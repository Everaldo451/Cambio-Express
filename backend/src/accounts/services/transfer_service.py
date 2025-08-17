from backend.core.services.currency_quotation.base import CurrencyQuotationService
from accounts.models import Account

class TransferService:
    
    def __init__(self, currency_quotation_service:CurrencyQuotationService):
        self.quotation_service = currency_quotation_service

    def calculate_converted_amount(self, from_currency:str, to_currency:str, amount):
        if from_currency == to_currency:
            return amount
        quotation = self.quotation_service.get_current_quotation(
            from_currency, to_currency
        )
        return amount/quotation

    def transfer_from_internal_account(self, from_account:Account, to_account:Account, amount):
        if amount > from_account.balance:
            raise ValueError("Insufficient balance.")
        
        converted_ammount = self.calculate_converted_amount(
            from_account.currency.code, to_account.currency.code, amount
        )
        
        from_account.balance -= amount
        to_account.balance += converted_ammount
        from_account.save()
        to_account.save()

    def transfer_from_external_account(self, to_account:Account, currency:str, amount):
        converted_ammount = self.calculate_converted_amount(
            currency, to_account.currency.code, amount
        )

        to_account.balance += converted_ammount
        to_account.save()



    
        