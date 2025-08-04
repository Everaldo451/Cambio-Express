from abc import ABC, abstractmethod

class CurrencyQuotationService(ABC):

    @abstractmethod
    def get_current_quotation(self, base_currency: str, target_currency: str) -> float:
        pass

    @abstractmethod
    def get_quotation_by_day(self, base_currency: str, target_currency: str) -> float:
        pass

    @abstractmethod
    def get_quotation_period(self, base_currency: str, target_currency: str, start, end) -> float:
        pass

