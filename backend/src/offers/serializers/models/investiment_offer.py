from rest_framework import serializers
from offers.models import InvestmentOffer
from finances.models import MonetaryIndex

import logging

class InvestmentOfferSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    monetary_index = serializers.SlugRelatedField(
        many=False,
        slug_field='symbol',
        queryset=MonetaryIndex.objects.all()
    )

    def get_created_by(self, obj):
        return obj.created_by.legal_id

    class Meta:
        model = InvestmentOffer
        fields = ["id","created_by","min_value","monetary_index","percent"]
        read_only_fields = ['id', 'created_by']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['created_by'] = user.company
        return super().create(validated_data)