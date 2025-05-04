from django.urls import path, include
from . import views, graphs

urlpatterns = [
   path("graphs/",include([
       path("get/<coin>",graphs.get)
   ])),
   path("feedbacks/",include([
       path("get/", views.get_feedbacks),
       path("set/",views.set_user_feedback)
   ])),
   path("getcsrf/",views.get_csrf),
]