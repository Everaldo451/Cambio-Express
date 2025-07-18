from rest_framework import viewsets, permissions
from rest_framework.decorators import action
import logging

from backend.core.permissions import IsSelfOrAdmin, IsNotAuthenticated

from users.models import User
from users.serializers.models import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_permissions(self):
		if self.request.method == "POST":
			return [IsNotAuthenticated()]
		return [permissions.IsAuthenticated(), IsSelfOrAdmin()]
	
	@action(detail=False, methods=["GET"], permission_classes=(permissions.IsAuthenticated,))
	def me(self, request):
		serializer = self.get_serializer(request.user)
		return Response(serializer.data)
