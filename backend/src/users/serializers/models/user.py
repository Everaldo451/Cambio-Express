from django.db import transaction
from rest_framework import serializers

from backend.core.enums import UserTypes

from users.models import User

from companies.serializers.models import CompanySerializer
from companies.models import Company

class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer(required=False)

	class Meta:
		model = User
		fields = ["id", "first_name", "last_name", "email", "password", "is_staff", "company"]
		read_only_fields = ['id']
		extra_kwargs = {
			'password': {'write_only': True}
		}

	@transaction.atomic
	def create(self, validated_data:dict):
		company_data = validated_data.pop("company", None)
		user = User.objects.create_user(**validated_data)

		if company_data is not None:
			user.user_type = UserTypes.COMPANY.value
			user.save()
			Company.objects.create(**company_data, user=user)
		return user