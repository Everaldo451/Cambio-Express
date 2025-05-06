from rest_framework import serializers
from .models import Offert, Account

class OffertSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source="company.name")
    company_phone = serializers.CharField(source="company.phone")

    class Meta:
        model = Offert
        fields = ["company_name","company_phone","code","min_value","index_variable","percent"]
        read_only_fields = ['__all__']


class AccountSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="user.email")

    class Meta:
        model = Account
        fields = ["email","code","balance"]
        read_only_fields = ['__all__']