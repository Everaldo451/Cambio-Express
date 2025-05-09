from django.http import HttpRequest
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from api.models import FeedBack
from api.serializers.common import PostFeedbackSerializer
from api.serializers.models import FeedBackSerializer

import logging


class FeedbackList(APIView):

	def get_permissions(self):
		if self.request.method == "POST":
			return [IsAuthenticated]
		return [IsAdminUser]


	def get(self, request:HttpRequest|Request, format=None):
		try:
			feedbacks = FeedBack.objects.all()
			serializer = FeedBackSerializer(feedbacks, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response({"message":"Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
		
	@method_decorator(csrf_protect)
	def post(self, request:HttpRequest|Request, format=None):
		serializer = PostFeedbackSerializer(data=request.data)
		if not serializer.is_valid():
			return Response({"message": "Invalid data. Bad request", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	
		user = request.user
		if hasattr(user, "company"):
			return Response({"message": "Companys cannot send a feedback."}, status=status.HTTP_403_FORBIDDEN)
	
		try:
			newFeedback = FeedBack(user=user, **serializer.validated_data)
			newFeedback.save()

			return Response({"message": "Feedback created successful;"}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({"Internal server Error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["GET"])
def search_feedbacks(request:HttpRequest):

	results = None
	try:
		last_feedbacks = FeedBack.objects.order_by("-id")[:5]
		results = FeedBackSerializer(last_feedbacks, many=True)
	except Exception as e: 
		return Response({"message":"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		
	try:
		if request.user is not AnonymousUser:
			feedback = FeedBack.objects.get(user=request.user)
			serialized = FeedBackSerializer(feedback)
			results.data.append(serialized.data) 
	except Exception as e:
		return Response({"message":"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	return Response({"message":"Feedbacks fetched sucessful.", "feedbacks":results.data}, status=status.HTTP_200_OK)