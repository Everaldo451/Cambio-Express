from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from offerts.models import Offert
from offerts.serializers.models import OffertSerializer
# Create your views here.


@api_view(["GET"])
def last_five_offerts(request, coin, index_var):
    try :
        offerts = Offert.objects.filter(coin=coin,indexVar=index_var).order_by("-id")[:5]
        serialized = OffertSerializer(offerts, many=True)
        return Response(serialized.data)
    except: return Response(None)
