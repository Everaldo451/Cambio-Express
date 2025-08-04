from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer, TokenRefreshSerializer
from drf_yasg.utils import swagger_auto_schema


class RefreshView(TokenRefreshView):
	@swagger_auto_schema(
		request_body=TokenRefreshSerializer,
	)
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)
	pass

class LogoutView(TokenBlacklistView):
	@swagger_auto_schema(
		request_body=TokenBlacklistSerializer
	)
	def post(self, request, *args, **kwargs):
		return super().post(request, *args, **kwargs)
	pass
