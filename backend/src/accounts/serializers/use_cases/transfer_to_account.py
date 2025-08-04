from rest_framework import serializers

class TransferToAccountSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=15, decimal_places=2, min_value=0.01)