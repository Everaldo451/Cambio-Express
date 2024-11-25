from django.shortcuts import redirect
from django.http import HttpRequest
from django.middleware.csrf import get_token
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FeedBacks
from .form import SetFeedbackForm
from .serializers import FeedBackSerializer

@api_view(["GET"])
def get_csrf(request):
	return Response(get_token(request))


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
