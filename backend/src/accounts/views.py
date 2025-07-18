from rest_framework import status, viewsets, permissions

from backend.core.permissions import IsOwnerOrAdmin

from accounts.models import Account
from accounts.serializers.models.account import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

    def get_permissions(self):
        if self.request.method=="POST":
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsOwnerOrAdmin()]
