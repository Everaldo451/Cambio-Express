from rest_framework import serializers
from feedbacks.models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(source="user.first_name")

	class Meta:
		model = FeedBack
		fields = ["first_name","comment","date"]
		read_only_fields = ['__all__']

