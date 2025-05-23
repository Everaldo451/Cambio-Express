from rest_framework import serializers

class GoogleOAuthSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=200, required=False)
    state = serializers.CharField(max_length=50, required=False)
    error = serializers.CharField(max_length=100, required=False)

    def validate(self, data):
        return super().validate(data)