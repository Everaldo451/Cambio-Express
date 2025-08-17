import django_filters
from offers.models import InvestmentOffer

class InvestmentOfferFilter(django_filters.FilterSet):
    min_value = django_filters.NumberFilter(field_name="min_value", lookup_expr="lte")
    percent_min = django_filters.NumberFilter(field_name="percent", lookup_expr="gte")
    percent_max = django_filters.NumberFilter(field_name="percent", lookup_expr="lte")

    class Meta:
        model = InvestmentOffer
        fields = ['monetary_index']