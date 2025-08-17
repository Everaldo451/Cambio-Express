from enum import Enum

class DataFrequencies(Enum):
    DAILY = "daily"
    MONTHLY = "monthly"
    ANNUALLY = "annualy"


class CalculationTypes(Enum):
    ACCUMULATED = "accumulated"
    CALCULATED = "calculated"
