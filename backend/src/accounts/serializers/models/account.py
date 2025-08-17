from rest_framework import serializers
from accounts.models import Account
from finances.models import Currency

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='created_by.email')
    currency = serializers.SlugRelatedField(
        many=False,
        slug_field="code",
        queryset=Currency.objects.all()
    )

    class Meta:
        model = Account
        fields = ["id", "user", "currency", "balance"]
        read_only_fields = ['id', "user", "balance"]

    def validate(self, data):
        user = self.context.get("request").user
        currency = data.get("currency")

        if self.instance:
            if Account.objects.filter(
                created_by=self.instance.user, currency=currency
            ).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError({"currency": "Account with current currency already exists"})
        else:
            if Account.objects.filter(created_by=user, currency=currency).exists():
                raise serializers.ValidationError({"currency": "Account with current currency already exists"})
        return data

    def create(self, validated_data):
        user = self.context.get('request').user
        return Account.objects.create(**validated_data, created_by=user)
