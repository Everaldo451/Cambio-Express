from rest_framework import serializers
from django.contrib.auth import authenticate
from users.serializers.models.user import UserSerializer

class PasswordLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("E-mail ou senha inválidos.")

        if not user.is_active:
            raise serializers.ValidationError("Esta conta está desativada.")
        data['user'] = user
        return data

class PasswordLoginResponseSerializer(serializers.Serializer):
    user = UserSerializer
    tokens = serializers.DictField(child=serializers.DictField())
