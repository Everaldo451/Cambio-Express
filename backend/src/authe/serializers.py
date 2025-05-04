from rest_framework import serializers
from . import models
from api.serializers import CompanySerializer

class UserSerializer(serializers.ModelSerializer):
	company = CompanySerializer()

	class Meta:
		model = models.User
		fields = ["id","first_name","email","company","money"]
		read_only_fields = ['__all__']