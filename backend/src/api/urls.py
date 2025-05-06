from django.urls import path, include
from . import views, graphs

urlpatterns = [
   path("graphs/",include([
       path("get/<coin>",graphs.get)
   ])),
   path("feedbacks/",include([
       path("",views.FeedbackList.as_view()),
       path("search/", views.search_feedbacks),
   ])),
   path("getcsrf/",views.get_csrf),
]