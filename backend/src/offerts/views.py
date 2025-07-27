from rest_framework import viewsets, mixins, permissions, pagination
from django_filters.rest_framework import DjangoFilterBackend

from offerts.models import Offert
from offerts.serializers.models import OffertSerializer
from .filter import OffertFilter

from backend.core.permissions import IsOwner


class OffertViewSet(viewsets.ModelViewSet):
    serializer_class = OffertSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OffertFilter

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Offert.objects.all()
        elif self.request.method in permissions.SAFE_METHODS or self.request.method == "POST":
            return Offert.objects.all()
        elif self.request.user.is_authenticated:
            return Offert.objects.filter(created_by=self.request.user)
        return Offert.objects.none()

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        elif self.request.method not in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated(), IsOwner()]
        return []


class OffertSearchViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Offert.objects.all()
    serializer_class = OffertSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OffertFilter
    
