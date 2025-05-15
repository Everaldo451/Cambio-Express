from rest_framework import serializers
from users.models import User
from companies.serializers.models import CompanySerializer

class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer()

	class Meta:
		model = User
		fields = ["id", "first_name", "last_name", "email", "company"]
		read_only_fields = ['__all__']

	def create(self, validated_data:dict):

		company_data = validated_data.get("company")
		if company_data:
			validated_data.pop("company")
		user = User.objects.create(**validated_data)
		return user