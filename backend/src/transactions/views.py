from rest_framework import viewsets, mixins, permissions

from .models import Transaction
from .serializers.models import TransactionSerializer

from backend.core.permissions import IsOwnerOrAdmin, IsCompanyUser

class TransactionViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):
    serializer_class = TransactionSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(), IsOwnerOrAdmin(),)
        return (permissions.IsAuthenticated(), IsCompanyUser(),)
    
    def get_queryset(self):
        user = self.request.user
        if self.request.method not in permissions.SAFE_METHODS:
            return Transaction.objects.all()
        elif user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(created_by=user)
