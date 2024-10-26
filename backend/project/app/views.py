from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.serializers import ListSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from requests import request as rq
from matplotlib import pyplot as plt
from .models import User, FeedBacks
from .form import ConfigForm
from .serializers import UserSerializer, FeedBackSerializer

@api_view(["GET"])
def get_csrf(request):
	return Response({"csrf":get_token(request)})


@api_view(["GET"])
def get_user(request):

	if request.COOKIES.get("access"):

		try:

			access = AccessToken(request.COOKIES.get("access"))
			user = User.objects.get(id=access.payload.get("id"))


			serializer = UserSerializer(user)
			serializer = serializer.data
			serializer.pop("id")

			return Response(serializer)

		except Exception as e: 
			return Response(None)
	
	else:
		return Response(None)
	
	"""elif request.COOKIES.get("refresh"):

		refresh = RefreshToken(request.COOKIES.get("refresh"))

		user = User.objects.get(id=refresh.payload.get("id"))

		serializer = UserSerializer(user)
		serializer = serializer.data
		serializer.pop("id")

		response = Response({"current_user":serializer})
		response.set_cookie("access",refresh.access_token,httponly=True,max_age=refresh.access_token.lifetime)

		return response
	"""

@api_view(["GET"])
def get_feedbacks(request):

	serialized = None

	if request.COOKIES.get("access"):

		try:

			access = AccessToken(request.COOKIES.get("access"))
			user = User.objects.get(id=access.payload.get("id"))

			feedback = FeedBacks.objects.get(user=user)

			serialized = FeedBackSerializer(feedback)

		except: pass

	try:
		last_feedbacks = FeedBacks.objects.order_by("-id")[:5]
		results = FeedBackSerializer(last_feedbacks, many=True)

		if serialized is not None:

			results.data.append(serialized.data)
		
		return Response(results.data)

	except Exception as e: 
		print(e)
		return Response(None)


@api_view(["POST"])
def set_user_feedback(request):

	rq = HttpRequest()
	rq.POST.get

	if request.COOKIES.get("access"):

		try:

			access = AccessToken(request.COOKIES.get("access"))
			user = User.objects.get(id=access.payload.get("id"))


			feedback = FeedBacks.objects.get(user=user)
			if feedback: raise Exception
			comment = request.POST.get("comment")
			stars = int(request.POST.get("stars"))

			newFeedback = FeedBacks(user=user, comment=comment, stars=stars)
			newFeedback.save()
		
		except: pass

	return redirect("http://localhost:3000")




# Create your views here.
