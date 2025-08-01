from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Account
        fields = ["id", "user", "code", "balance"]
        read_only_fields = ['id', "user", "balance"]

    def validate(self, data):
        user = self.context.get("request").user
        code = data.get("code")

        if self.instance:
            if Account.objects.filter(
                created_by=self.instance.user, code=code
            ).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError({"code": "Account with current code already exists"})
        else:
            if Account.objects.filter(created_by=user, code=code).exists():
                raise serializers.ValidationError({"code": "Account with current code already exists"})
        return data

    def create(self, validated_data):
        user = self.context.get('request').user
        return Account.objects.create(**validated_data, created_by=user)
