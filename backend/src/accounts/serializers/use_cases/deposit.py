from rest_framework import serializers

from backend.core.types.offers import CodeChoices

class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=15, decimal_places=2, min_value=0.01)
    currency = serializers.ChoiceField(
        choices=[(tag.name, tag.value.title()) for tag in CodeChoices]
    )