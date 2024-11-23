from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		fields = ["name", "phone", "CNPJ"]


class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer()

	class Meta:
		model = models.User
		fields = ["id","first_name","email","company","money"]
		read_only_fields = ['__all__']



class FeedBackSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(source="user.first_name")

	class Meta:
		model = models.FeedBacks
		fields = ["first_name","comment","date"]
		read_only_fields = ['__all__']
