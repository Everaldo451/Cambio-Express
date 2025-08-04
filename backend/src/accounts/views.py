from django.db import transaction

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action

from backend.core.permissions import IsOwnerOrAdmin

from accounts.models import Account
from accounts.serializers.models.account import AccountSerializer
from accounts.serializers.use_cases import TransferToAccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

    def get_permissions(self):
        if self.request.method=="POST":
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
    
    @action(methods=["POST"], detail=True, url_path="transfer/(?P<to_id>[^/.]+)")
    def transfer(self, request, pk=None, to_id=None):
        serializer = TransferToAccountSerializer(request.body)
        serializer.is_valid(raise_exception=True)

        from_account = None
        try:
            from_account = Account.objects.get(id=pk)
            to_account = Account.objects.get(id=to_id)
        except Account.DoesNotExist:
            return None
        
        amount = serializer.validated_data['amount']
        
        try:
            with transaction.atomic():
                from_account.balance -= amount
                from_account.save()
                to_account.balance += amount
                to_account.save()
            return
        except:
            return None
