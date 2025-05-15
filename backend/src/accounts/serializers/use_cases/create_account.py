from rest_framework import serializers
from accounts.models import CODE_CHOICES

class CreateAccountSerializer(serializers.Serializer):
    code = serializers.ChoiceField(choices=CODE_CHOICES)