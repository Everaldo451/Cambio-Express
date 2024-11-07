from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.User
		fields = ["id","username","email","is_staff","is_company"]
		read_only_fields = ['__all__']


class FeedBackSerializer(serializers.ModelSerializer):

	username = serializers.CharField(source="user.username")

	class Meta:
		model = models.FeedBacks
		fields = ["username","comment","stars"]
		read_only_fields = ['__all__']