from django.urls import path, include
from . import views

urlpatterns = [
    path("getmany/<coin>/<indexVar>", views.get_offerts)
]
