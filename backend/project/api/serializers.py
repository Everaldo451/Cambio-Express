from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		fields = ["name", "phone", "CNPJ"]

class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer()

	class Meta:
		model = models.User
		fields = ["id","username","email","is_staff","company"]
		read_only_fields = ['__all__']


class FeedBackSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source="user.username")

	class Meta:
		model = models.FeedBacks
		fields = ["username","comment","stars"]
		read_only_fields = ['__all__']