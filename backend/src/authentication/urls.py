from django.urls import path, include
from . import views

urlpatterns = [
    path("login/",views.password_login,name="login"),
    path("register/", views.PasswordRegister.as_view()),
    path("logout/",views.logout,name="logout"),
    path("google/", include([
        path("redirect/", views.google_auth_redirect),
        path("callback/", views.google_auth_callback, name="oauth2callback")
    ]))
]
