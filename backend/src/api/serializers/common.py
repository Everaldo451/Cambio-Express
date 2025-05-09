from rest_framework import serializers


class PostFeedbackSerializer(serializers.Serializer):

    comment = serializers.CharField()
