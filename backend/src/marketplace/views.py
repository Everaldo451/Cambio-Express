from django.http import HttpRequest
from django.db import DatabaseError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from .models import Offert, Account
from .form import PostAccountForm
from .serializers import OffertSerializer

class AccountList(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated]
        return []
    
    def post(self, request:Request, format=None):
        post_form = PostAccountForm(request.data)
        if not post_form.is_valid():
            return Response({"message":"Invalid data. Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            account = Account(user=request.user, **post_form.cleaned_data)
            account.save()
            return Response({"message":"Account created successful."}, status=status.HTTP_200_OK)
        except DatabaseError as error:
            return Response({"message":"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_offerts(request, coin, indexVar):

    try :
        
        offerts = Offert.objects.filter(coin=coin,indexVar=indexVar).order_by("-id")[:5]
        serialized = OffertSerializer(offerts, many=True)

        return Response(serialized.data)
    
    except: return Response(None)
