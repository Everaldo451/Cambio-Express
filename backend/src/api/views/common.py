from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging

@api_view(["GET"])
def get_csrf(request):
	return Response({"data":get_token(request)})

