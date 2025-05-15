from django.urls import path, include
from .views import UserList, UserDetails

urlpatterns = [
    path("", UserList.as_view()),
    path("<int:id>/", UserDetails.as_view())
]