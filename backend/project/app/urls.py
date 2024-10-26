from django.urls import path, include
from . import views, auth, graphs

urlpatterns = [
   path("auth/",include([
       path("login/",auth.login,name="login"),
       path("register/",auth.register,name="register"),
       path("logout/",auth.logout,name="logout")
   ])),
   path("graphs/",include([
       path("get/<coin>",graphs.get)
   ])),
   path("feedbacks/",include([
       path("get/", views.get_feedbacks)
   ])),
   path("getcsrf/",views.get_csrf),
   path("getuser/",views.get_user),
]