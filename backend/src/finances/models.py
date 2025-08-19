from django.db import models
from backend.core.types.finances import DataFrequencies, CalculationTypes

class Currency(models.Model):
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=10) #BRL, USD, EUR
    symbol = models.CharField(max_length=5) #$, R$

    def __str__(self):
        return self.name


class MonetaryIndex(models.Model):
    currency = models.ForeignKey(
        'finances.Currency',
        models.CASCADE
    )
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20) #IPCA, SELIC
    api_config = models.OneToOneField(
        "apis.APIConfig",
        models.DO_NOTHING
    )
    data_frequency = models.TextField(
        choices=[(dt_frequency.value, dt_frequency.value.title()) for dt_frequency in DataFrequencies]
    )
    calculation_type = models.TextField(
        choices=[(calc_type.value, calc_type.value.title()) for calc_type in CalculationTypes]
    )
