from rest_framework import serializers
from api.models import CODE_CHOICES

class PostAccountSerializer(serializers.Serializer):
    code = serializers.ChoiceField(choices=CODE_CHOICES)


