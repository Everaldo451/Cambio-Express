from rest_framework import serializers
from offers.models import InvestmentOffer

import logging

class InvestmentOfferSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.company.name

    class Meta:
        model = InvestmentOffer
        fields = ["id","created_by","code","min_value","index_variable","percent"]
        read_only_fields = ['id', 'created_by']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['created_by'] = user
        return super().create(validated_data)