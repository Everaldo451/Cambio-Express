import django_filters
from offerts.models import Offert

class OffertFilter(django_filters.FilterSet):
    min_value = django_filters.NumberFilter(field_name="min_value", lookup_expr="lte")
    code = django_filters.CharFilter(field_name="code", lookup_expr="exact")
    index_variable = django_filters.CharFilter(field_name="index_variable", lookup_expr="exact")
    percent_min = django_filters.NumberFilter(field_name="percent", lookup_expr="gte")
    percent_max = django_filters.NumberFilter(field_name="percent", lookup_expr="lte")

    class Meta:
        model = Offert
        fields = []