from rest_framework.decorators import api_view
from rest_framework.response import Response

from offerts.models import Offert
from offerts.serializers.models import OffertSerializer

from core.db import get_n_last_obj


@api_view(["GET"])
def last_five_offerts(request, coin, index_var):
    get_5_last_offerts_data = get_n_last_obj(Offert, 5)
    if get_5_last_offerts_data["error"]:
        return Response(
            {"message": get_5_last_offerts_data["message"]}, 
            status=get_5_last_offerts_data["status"]
        )
    
    offerts = get_5_last_offerts_data["obj"]
    serializer = OffertSerializer(offerts, many=True)
    return Response(serializer.data, status=get_5_last_offerts_data["status"])
