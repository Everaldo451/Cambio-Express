from rest_framework import serializers
from users.models import Company

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ["id", "name", "legal_id"]
		read_only_fields = ['id']

