from django.db import DatabaseError
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

from api.models import Account

from marketplace.serializers import PostAccountSerializer

class AccountList(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return []
    
    @method_decorator(csrf_protect)
    def post(self, request:Request, format=None):
        serializer = PostAccountSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message":"Invalid data. Bad request", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            data = serializer.validated_data
            if Account.objects.filter(user=request.user, code=data.get("code")).exists():
                return Response({"message":"Account with current code already exists"}, status=status.HTTP_409_CONFLICT)
            account = Account(user=request.user, **data)
            account.save()
            return Response({"message":"Account created successful."}, status=status.HTTP_201_CREATED)
        except DatabaseError as error:
            return Response({"message":"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
