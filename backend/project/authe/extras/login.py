from django.contrib.auth import authenticate
from ..form import LoginForm
from rest_framework.response import Response
from rest_framework import status
from ..utils import generate_tokens

def login(request):

	form = LoginForm(request.POST)

	if form.is_valid():

		user = authenticate(
			request,
			username = form.cleaned_data.get("email"),
			password = form.cleaned_data.get("password")
		)

		if user is None or not user.is_active:

			print("No user")
			return Response("No user", status=status.HTTP_401_UNAUTHORIZED)

		return generate_tokens(request, user)
		
	
	return Response(None, status=status.HTTP_401_UNAUTHORIZED)	
