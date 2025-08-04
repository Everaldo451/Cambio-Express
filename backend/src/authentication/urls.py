from django.urls import path, include
from .views import LogoutView, RefreshView
from .oauth.google.views import google_auth_redirect, GoogleOauthCallback
from .password.views import PasswordLogin

urlpatterns = [
    path("login/",PasswordLogin.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("refresh/",RefreshView.as_view(),name="refresh"),
    path("google/", include([
        path("redirect/", google_auth_redirect),
        path("callback/", GoogleOauthCallback.as_view(), name="oauth2callback")
    ]))
]
