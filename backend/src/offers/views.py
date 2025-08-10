from rest_framework import viewsets, mixins, permissions, pagination
from django_filters import rest_framework as filters

from offers.models import InvestmentOffer
from offers.serializers.models import InvestmentOfferSerializer
from .filter import InvestmentOfferFilter

from backend.core.permissions import IsCompanyOwner, IsCompanyUser


class InvestmentOfferViewSet(viewsets.ModelViewSet):
    serializer_class = InvestmentOfferSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InvestmentOfferFilter

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return InvestmentOffer.objects.all()
        elif self.request.method in permissions.SAFE_METHODS or self.request.method == "POST":
            return InvestmentOffer.objects.all()
        elif self.request.user.is_authenticated:
            return InvestmentOffer.objects.filter(created_by=self.request.user)
        return InvestmentOffer.objects.none()

    def get_permissions(self):
        if self.request.method == "POST":
            return (permissions.IsAuthenticated(), IsCompanyUser(),)
        elif self.request.method not in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(), IsCompanyUser(), IsCompanyOwner(),)
        return []
    
