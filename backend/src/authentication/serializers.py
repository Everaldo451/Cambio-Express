from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=100)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    full_name = serializers.CharField(max_length=100, required=False)
    CNPJ = serializers.CharField(max_length=14, required=False)
    name = serializers.CharField(max_length=254, required=False)
    is_company = serializers.BooleanField()

    def validate(self, data:dict):
        if data["is_company"]:
            if not data.get("CNPJ") or not data.get("name"):
                raise serializers.ValidationError("Company fields are required")
            
            data.pop("full_name", None)
            
        else:
            full_name:str = data.get("full_name")
            if not full_name:
                raise serializers.ValidationError("User fields are required")
        
            try:
                splited = full_name.split(maxsplit=1)
                data["first_name"] = splited[0]
                data["last_name"] = splited[1]
            except IndexError as error:
                raise serializers.ValidationError("You need to send a valid full name.")
            
            data.pop("CNPJ", None)
            data.pop("name", None)
        
        return data
    

class OAuthSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=200, required=False)
    state = serializers.CharField(max_length=50, required=False)
    error = serializers.CharField(max_length=100, required=False)

    def validate(self, data):
        return super().validate(data)