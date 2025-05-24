from django.http import HttpRequest

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from feedbacks.models import FeedBack
from feedbacks.serializers.use_cases import CreateFeedbackSerializer
from feedbacks.serializers.models import FeedBackSerializer

from core.db import get_all_obj, get_n_last_obj
import logging


class FeedbackList(APIView):

	def get_permissions(self):
		if self.request.method == "POST":
			return [IsAuthenticated()]
		return [IsAdminUser()]


	def get(self, request:HttpRequest|Request, format=None):
		get_feedbacks_data = get_all_obj(FeedBack)
		if get_feedbacks_data["error"]:
			return Response({"message":get_feedbacks_data["message"]},status=get_feedbacks_data["status"])
		
		users = get_feedbacks_data["obj"]
		serializer = FeedBackSerializer(users, many=True)
		return Response(serializer.data, status=get_feedbacks_data["status"])
		
		
	def post(self, request:HttpRequest|Request, format=None):
		serializer = CreateFeedbackSerializer(data=request.data)
		if not serializer.is_valid():
			return Response({"message": "Invalid data. Bad request", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	
		user = request.user
		if user.company.exists():
			return Response({"message": "Companys cannot send a feedback."}, status=status.HTTP_403_FORBIDDEN)
	
		try:
			newFeedback = FeedBack(user=user, **serializer.validated_data)
			newFeedback.save()

			return Response({"message": "Feedback created successful;"}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({"Internal server Error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["GET"])
def search_feedbacks(request:HttpRequest):

	get_5_last_feedbacks_data = get_n_last_obj(FeedBack, 5)
	if get_5_last_feedbacks_data["error"]:
		return Response({"message":get_5_last_feedbacks_data["message"]}, status=get_5_last_feedbacks_data["status"])
	
	last_feedbacks = get_5_last_feedbacks_data["obj"]
	serializer = FeedBackSerializer(last_feedbacks, many=True)
	return Response(serializer.data, status=get_5_last_feedbacks_data["status"])