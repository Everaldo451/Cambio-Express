from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		fields = ["name", "phone", "CNPJ"]


class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer()
	first_name = serializers.SerializerMethodField()

	class Meta:
		model = models.User
		fields = ["id","first_name","email","company","money"]
		read_only_fields = ['__all__']

	def get_first_name(self, obj):
		first_name = obj.user.full_name.split()[0]
		return first_name


class FeedBackSerializer(serializers.ModelSerializer):
	first_name = serializers.SerializerMethodField()

	class Meta:
		model = models.FeedBacks
		fields = ["first_name","comment","date"]
		read_only_fields = ['__all__']

	def get_first_name(self, obj):
		first_name = obj.user.full_name.split()[0]
		return first_name
