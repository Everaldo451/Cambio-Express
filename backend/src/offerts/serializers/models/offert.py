from rest_framework import serializers
from offerts.models import Offert

class OffertSerializer(serializers.ModelSerializer):

    created_by = serializers.CharField(source="created_by.company.name")

    class Meta:
        model = Offert
        fields = ["id","created_by","code","min_value","index_variable","percent"]
        read_only_fields = ['id', 'created_by']