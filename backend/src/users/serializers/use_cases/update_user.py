from rest_framework import serializers
from users.models import User

class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {
            'first_name': {
                'required': False,
            },
            'last_name': {
                'required': False,
            },
            'email': {
                'required': False,
            },
            'password': {
                'required': False,
                'write_only': True
            }
        }


    def validate(self, attrs):
        if len(attrs)==0:
            raise serializers.ValidationError("You need to change one or more attributes.")
        return super().validate(attrs)


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value


    def update(self, instance:User, validated_data:dict):
        password = validated_data.get('password')
        if password is not None:
            instance.set_password(password)

        for key, value in validated_data.items():
            if value is None or key=="password":
                continue

            setattr(instance, key, value)

        instance.save()
        return instance
