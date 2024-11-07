from rest_framework import serializers
from .models import Offert

class OffertSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source="company.name")
    company_phone = serializers.CharField(source="company.phone")

    class Meta:
        model = Offert
        fields = ["company_name","company_phone","coin","value","index_variable","fees"]
        read_only_fields = ['__all__']