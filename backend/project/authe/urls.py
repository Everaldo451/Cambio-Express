from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.password_login,name="login"),
    path("register/",views.password_register,name="register"),
    path("logout/",views.logout,name="logout"),
    path("getuser/",views.get_user),
    path("oauth/", views.oauth_client_url),
    path("oauthcall/", views.oauth_callback, name="oauth2callback")
]
