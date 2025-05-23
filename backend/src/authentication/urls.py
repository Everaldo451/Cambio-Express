from django.urls import path, include
from .views import logout
from .oauth.google.views import google_auth_redirect, GoogleOauthCallback
from .password.views import PasswordRegister, PasswordLogin

urlpatterns = [
    path("login/",PasswordLogin.as_view(),name="login"),
    path("register/", PasswordRegister.as_view()),
    path("logout/",logout,name="logout"),
    path("google/", include([
        path("redirect/", google_auth_redirect),
        path("callback/", GoogleOauthCallback.as_view(), name="oauth2callback")
    ]))
]
