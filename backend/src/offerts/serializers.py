from rest_framework import serializers
from offerts.models import Offert

class OffertSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source="company.name")
    company_phone = serializers.CharField(source="company.phone")

    class Meta:
        model = Offert
        fields = ["company_name","company_phone","code","min_value","index_variable","percent"]
        read_only_fields = ['__all__']

