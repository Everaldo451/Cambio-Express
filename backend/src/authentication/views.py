from rest_framework.decorators import api_view

from django.http import HttpRequest
from django.shortcuts import redirect


@api_view(["GET"])
def logout(request:HttpRequest):
	response = redirect("http://localhost:3000")
	response.delete_cookie("access_token")
	response.delete_cookie("refresh_token")
	return response
