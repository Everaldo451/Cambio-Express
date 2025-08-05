from rest_framework import serializers

from backend.core.types.offers import CodeChoices

class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=15, decimal_places=2, min_value=0.01)
    currency = serializers.CharField(
        max_length=10,
        choices=[(tag.name, tag.value.title()) for tag in CodeChoices]
    )