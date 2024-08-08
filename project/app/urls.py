from django.urls import path, include
from . import views, auth

urlpatterns = [
   path("auth/",include([
       path("login/",auth.login,name="login"),
       path("register/",auth.register,name="register")
   ])),
   path("",include([
       path("",views.home,name="home"),
       path("login/",views.login,name="loginview")
   ]))
]