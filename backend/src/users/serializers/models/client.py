from rest_framework import serializers
from users.models import Client

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ['id', 'first_name', 'last_name']
		read_only_fields = ['id']

