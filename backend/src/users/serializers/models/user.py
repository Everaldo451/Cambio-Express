from django.db import transaction
from rest_framework import serializers

from backend.core.types.user import UserTypes

from users.models import User, Client, Company
from users.serializers.models import ClientSerializer, CompanySerializer

class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer(required=False)
	client = ClientSerializer(required=False)

	class Meta:
		model = User
		fields = ["id", "email", "password", "is_staff", "company", "client"]
		read_only_fields = ['id', 'is_staff']
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def validate(self, attrs):
		user_type_data_fields = ['company', 'client']

		user_type_counter = 0
		for user_type_data_field in user_type_data_fields:
			data = attrs.get(user_type_data_field)
			if data is not None:
				user_type_counter+=1

		if user_type_counter==0:
			raise serializers.ValidationError({'user_type': 'The user must be one type.'})
		elif user_type_counter>1:
			raise serializers.ValidationError({'user_type': 'The user must be only one type.'})
		return attrs

	@transaction.atomic
	def create(self, validated_data:dict):
		user_type_and_model_per_field = {
			'company': {
				'user_type': UserTypes.COMPANY.value,
				'model': Company
			},
			'client': {
				'user_type': UserTypes.STANDARD.value,
				'model': Client
			}
		}
		user_type_data = None
		field_data = None
		for field, user_type_and_model in user_type_and_model_per_field.items():
			data = validated_data.pop(field, None)
			if data is not None:
				field_data = data
				user_type_data = user_type_and_model

		#company_data = validated_data.pop("company", None)
		#client_data = validated_data.pop("client", None)
		user = User.objects.create_user(**validated_data)

		user.user_type = user_type_data['user_type']
		user.save()
		user_type_data['model'].objects.create(**field_data, user=user)

		"""
		if company_data is not None:
			user.user_type = UserTypes.COMPANY.value
			user.save()
			Company.objects.create(**company_data, user=user)
		"""
		return user