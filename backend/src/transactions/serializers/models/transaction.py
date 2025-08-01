from django.db import transaction
from rest_framework import serializers
from transactions.models import Transaction
from offers.models import InvestmentOffer
from accounts.models import Account

class TransactionSerializer(serializers.ModelSerializer):
    investment_offer = serializers.SlugRelatedField(
        queryset = InvestmentOffer.objects.all(),
        many = False,
        read_only = False,
        slug_field = 'id'
    )   
    buyer = serializers.SerializerMethodField()

    def get_buyer(self, obj):
        return obj.created_by.email

    class Meta:
        model = Transaction
        fields = ['id', 'buyer', 'value', 'investment_offer', 'created_at']
        read_only_fields = ['id', 'buyer', 'created_at']

    def validate(self, data):
        request = self.context.get('request')
        user = request.user
        investment_offer = data.get('investment_offer')

        if not self.instance:
            try:
                account = Account.objects.get(created_by=user, code=investment_offer.code)
            except Account.DoesNotExist:
                raise serializers.ValidationError({
                'investment_offer': 'You need an account in the currency of this offer to perform this transaction.'
            })
            value = data.get('value')
            if account.balance < value:
                raise serializers.ValidationError({
                    'value': 'The amount of money in the transaction exceeded that in the account.'
                })
            data['account_instance'] = account
        return data

    @transaction.atomic
    def create(self, validated_data):
        transaction_value = validated_data.get('value')
        account = validated_data.pop('account_instance')
        account.balance -= transaction_value
        account.save()

        request = self.context.get('request')
        user = request.user
        validated_data['created_by'] = user
        return super().create(validated_data)