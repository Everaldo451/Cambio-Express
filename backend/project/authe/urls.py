from django.urls import path, include
from . import views

urlpatterns = [
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.logout,name="logout"),
    path("getuser/",views.get_user),
    path("getjwt/", views.get_jwt)
]
