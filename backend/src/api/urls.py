from django.urls import path, include
from .views import graphs

urlpatterns = [
    path("feedbacks/",include("feedbacks.urls")),
    path("offerts/", include("offerts.urls")),
    path("auth/", include("authentication.urls")),
    path("graphs/",include([
        path("get/<coin>",graphs.get)
    ])),
]