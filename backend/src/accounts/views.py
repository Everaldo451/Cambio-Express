from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.core.permissions import IsOwner, IsOwnerOrAdmin
from backend.core.services.currency_quotation.bcb_quotation import BCBCurrencyQuotationService

from accounts.models import Account
from accounts.serializers.models.account import AccountSerializer
from accounts.serializers.use_cases import TransferToAccountSerializer, DepositSerializer
from accounts.services.transfer_service import TransferService

class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

    def get_permissions(self):
        if self.request.method=="POST":
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
    
    @action(
        methods=["POST"], 
        detail=True, 
        url_path="transfer/(?P<to_id>[^/.]+)", 
        permission_classes = [permissions.IsAuthenticated(), IsOwner()] 
    )
    def transfer(self, request, pk=None, to_id=None):
        serializer = TransferToAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        from_account = get_object_or_404(Account, id=pk)
        to_account = get_object_or_404(Account, id=to_id)
        
        self.check_object_permissions(request, from_account)
        self.check_object_permissions(request, to_account)
        
        amount = serializer.validated_data['amount']
        quotation_service = BCBCurrencyQuotationService()
        transfer_service = TransferService(quotation_service)
        
        try:
            with transaction.atomic():
                transfer_service.transfer_from_internal_account(
                    from_account, to_account, amount
                )
            response_data={
                "from_account": self.get_serializer(from_account).data,
                "to_account": self.get_serializer(to_account).data
            }
            return Response(response_data,status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Unexpected error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(
        methods=["POST"], 
        detail=True, 
        url_path="deposit", 
        permission_classes = [permissions.IsAuthenticated(), IsOwner()] 
    )
    def deposit(self, request, pk=None):
        serializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        to_account = get_object_or_404(Account, id=pk)
        self.check_object_permissions(request, to_account)
        
        amount = serializer.validated_data['amount']
        currency = serializer.validated_data['currency']
        quotation_service = BCBCurrencyQuotationService()
        transfer_service = TransferService(quotation_service)
        
        try:
            with transaction.atomic():
                transfer_service.transfer_from_external_account(
                    to_account, currency, amount
                )
            account_serializer = self.get_serializer(to_account)
            return Response(account_serializer.data,status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Unexpected error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
