from django.urls import path, include
from . import views

urlpatterns = [
    path("getmany/<coin>/<indexVar>", views.get_offerts),
    path("account/", include([
        path("", views.AccountList.as_view())
    ]))
]
