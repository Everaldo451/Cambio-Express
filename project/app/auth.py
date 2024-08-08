from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def login(request):
	
	return Response({'user':None})
	

@api_view(["POST"])
def register(request):
	
	return Response({'user':None})