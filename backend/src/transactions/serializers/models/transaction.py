from rest_framework import serializers
from transactions.models import Transaction
from offers.serializers.models import InvestmentOfferSerializer

class TransactionSerializer(serializers.ModelSerializer):
    investment_offer = InvestmentOfferSerializer()
    buyer = serializers.CharField(source='created_by.email')

    class Meta:
        model = Transaction
        fields = ['id', 'buyer', 'value', 'investment_offer', 'created_at']
        read_only_fields = ['id', 'created_at']