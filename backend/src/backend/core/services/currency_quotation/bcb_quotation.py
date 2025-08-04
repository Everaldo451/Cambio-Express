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
        date_format = f"{now.month:02d}-{now.day:02d}-{now.year}"
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
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            value = data.get('value')
            if not value or not isinstance(value, list):
                raise Exception('Quotation not found in response.')
            quotation_data = value[0]
            quotation = quotation_data.get('cotacaoCompra')
            if quotation is None:
                raise Exception('cotacaoCompra not found in quotation data.')
            return quotation
        except requests.RequestException as e:
            raise Exception(f'Internal server error. {e}')
        except ValueError:
            raise Exception('Response is not valid JSON.')

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