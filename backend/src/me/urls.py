from django.urls import path, include
from .views import MeDetails

urlpatterns = [
    path("", MeDetails.as_view()),
]