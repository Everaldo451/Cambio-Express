from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def healtycheck(request):
    return Response(status=status.HTTP_204_NO_CONTENT)