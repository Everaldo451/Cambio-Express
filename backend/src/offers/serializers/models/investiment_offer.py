from rest_framework import serializers
from offers.models import InvestmentOffer

class InvestmentOfferSerializer(serializers.ModelSerializer):

    created_by = serializers.CharField(source="created_by.company.name")

    class Meta:
        model = InvestmentOffer
        fields = ["id","created_by","code","min_value","index_variable","percent"]
        read_only_fields = ['id', 'created_by']