from django.shortcuts import redirect
from django.http import HttpRequest
from django.middleware.csrf import get_token
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import FeedBacks
from .form import SetFeedbackForm
from .serializers import UserSerializer, FeedBackSerializer
from authe.utils import generate_token_response

@api_view(["GET"])
def get_csrf(request):
	return Response(get_token(request))


@api_view(["GET"])
def get_jwt(request):

	if request.COOKIES.get("access_token") and request.COOKIES.get("refresh_token"):
		try:
			refresh = RefreshToken(request.COOKIES.get("refresh_token"))
			return generate_token_response(refresh)
		
		except: return Response(None)
	return Response(None)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):

	try:
		serializer = UserSerializer(request.user)
		serializer = serializer.data
		serializer.pop("id")
		if not request.user.groups.filter(name="Company").exists():
			print("notCompany")
			serializer.pop("company")

		return Response(serializer)

	except Exception as e: 
		return Response(None)
	
	


@api_view(["GET"])
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
