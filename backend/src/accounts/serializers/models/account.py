from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="user.email")

    class Meta:
        model = Account
        fields = ["email","code","balance"]
        read_only_fields = ['__all__']
