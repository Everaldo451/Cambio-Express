from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.middleware.csrf import get_token
from django.db import DataError
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from requests import request as rq
from matplotlib import pyplot as plt
from .models import User, FeedBacks
from .form import ConfigForm, SetFeedbackForm
from .serializers import UserSerializer, FeedBackSerializer

@api_view(["GET"])
def get_csrf(request):
	print(request.COOKIES)
	return Response({"csrf":get_token(request)})


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):

	try:
		serializer = UserSerializer(request.user)
		serializer = serializer.data
		serializer.pop("id")

		return Response(serializer)

	except Exception as e: 
		return Response(None)
	
	


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def get_feedbacks(request):

	try:
		last_feedbacks = FeedBacks.objects.order_by("-id")[:5]
		results = FeedBackSerializer(last_feedbacks, many=True)

	except Exception as e: 
		pass
		
	try:
		
		if request.user is not AnonymousUser:

			feedback = FeedBacks.objects.get(user=request.user)

			serialized = FeedBackSerializer(feedback)

			if results: results.data.append(serialized.data) 
	
	except: pass

	return Response(results.data if results else [serialized] if serialized else None)



@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def set_user_feedback(request):

	form = SetFeedbackForm(request.POST)

	if form.is_valid():

		print("ola")

		try:

			newFeedback = FeedBacks(user=request.user, **form.cleaned_data)
			newFeedback.save()
		
		except Exception as e: print(e)

	return redirect("http://localhost:3000")




# Create your views here.
