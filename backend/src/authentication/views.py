from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpRequest
from django.shortcuts import redirect


@api_view(["GET"])
def logout(request:HttpRequest):
	response = Response(status=status.HTTP_204_NO_CONTENT)
	response.delete_cookie("access_token")
	response.delete_cookie("refresh_token")
	return response
