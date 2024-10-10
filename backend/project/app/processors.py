from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import User
from .serializers import UserSerializer


def get_user(request):

	if request.COOKIES.get("access"):

		try:

			access = AccessToken(request.COOKIES.get("access"))

			user = User.objects.get(id=access.payload.get("id"))

			serializer = UserSerializer(user)
			serializer = serializer.data
			serializer.pop("id")

			return {"current_user":serializer}

		except: return {}
	
	else: return {}