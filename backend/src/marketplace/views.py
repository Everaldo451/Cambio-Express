from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Offert
from .serializers import OffertSerializer

@api_view(["GET"])
def get_offerts(request, coin, indexVar):

    try :
        
        offerts = Offert.objects.filter(coin=coin,indexVar=indexVar).order_by("-id")[:5]
        serialized = OffertSerializer(offerts, many=True)

        return Response(serialized.data)
    
    except: return Response(None)

# Create your views here.
