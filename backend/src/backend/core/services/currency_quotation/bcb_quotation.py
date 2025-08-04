from .base import CurrencyQuotationService
from datetime import datetime
from decimal import Decimal
import requests

class BCBCurrencyQuotationService(CurrencyQuotationService):

    def params_to_string(self, separator:str, params:dict):
        return separator.join(
            ["=".join([key, value]) for key, value in params.items()]
        )

    def get_current_quotation_real(self, base_currency):
        now = datetime.now()
        date_format = f"{now.day:02d}-{now.month:02d}-{now.year}"
        query_params = {
            '$format':'json',
            '$select':'cotacaoCompra',
            '$skip': '0',
            '$top': '1'
        }
        api_params = {
            'moeda':f"'{base_currency}'",
            'dataCotacao':f"'{date_format}'",
        }
        query_params_string = self.params_to_string('&', query_params)
        api_params_string = self.params_to_string(',', api_params)

        url = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia({api_params_string})?{query_params_string}'
        response = requests.get(url)
        json = response.json()
        return json.get('cotacaoCompra')

    def get_current_quotation(self, base_currency, target_currency):
        base_currency_quotation_real = Decimal(
            self.get_current_quotation_real(base_currency)
        )
        target_currency_currency_quotation_real = Decimal(
            self.get_current_quotation_real(target_currency)
        )
        return base_currency_quotation_real/target_currency_currency_quotation_real
    
    def get_quotation_by_day(self, base_currency, target_currency):
        return super().get_quotation_by_day(base_currency, target_currency)
    
    def get_quotation_period(self, base_currency, target_currency, start, end):
        return super().get_quotation_period(base_currency, target_currency, start, end)