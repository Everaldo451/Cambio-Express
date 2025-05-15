from rest_framework import serializers


class CreateFeedbackSerializer(serializers.Serializer):

    comment = serializers.CharField()