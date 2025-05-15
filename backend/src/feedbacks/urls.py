from django.urls import path, include
from .views import FeedbackList, search_feedbacks

urlpatterns = [
    path("", FeedbackList.as_view()),
    path("search/", search_feedbacks),
]