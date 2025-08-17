from rest_framework import serializers
from offers.models import InvestmentOffer

import logging

class InvestmentOfferSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.CNPJ

    class Meta:
        model = InvestmentOffer
        fields = ["id","created_by","min_value","monetary_index","percent"]
        read_only_fields = ['id', 'created_by']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['created_by'] = user.company
        return super().create(validated_data)