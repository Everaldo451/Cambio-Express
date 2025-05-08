from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		fields = ["name", "phone", "CNPJ"]


class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer()

	class Meta:
		model = models.User
		fields = ["id","first_name","email","company"]
		read_only_fields = ['__all__']


class FeedBackSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(source="user.first_name")

	class Meta:
		model = models.FeedBack
		fields = ["first_name","comment","date"]
		read_only_fields = ['__all__']


class OffertSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source="company.name")
    company_phone = serializers.CharField(source="company.phone")

    class Meta:
        model = models.Offert
        fields = ["company_name","company_phone","code","min_value","index_variable","percent"]
        read_only_fields = ['__all__']


class AccountSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="user.email")

    class Meta:
        model = models.Account
        fields = ["email","code","balance"]
        read_only_fields = ['__all__']
