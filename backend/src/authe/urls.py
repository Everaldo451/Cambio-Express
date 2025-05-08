from django.urls import path, include
from . import views

urlpatterns = [
    path("login/",views.password_login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("oauth/", views.oauth_client_url),
    path("oauthcall/", views.oauth_callback, name="oauth2callback")
]
