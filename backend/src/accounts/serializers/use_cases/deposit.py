from rest_framework import serializers

from finances.models import Currency

class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=15, decimal_places=2, min_value=0.01)
    currency = serializers.SlugRelatedField(
        slug_field = 'code',
        queryset = Currency.objects.all()
    )