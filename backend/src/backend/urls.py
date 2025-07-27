"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users import views as user_views
from accounts import views as account_views
from offers import views as offert_views

from decouple import config

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
router.register(r'accounts', account_views.AccountViewSet, basename='accounts')
router.register(r'offers', offert_views.InvestmentOfferViewSet, basename='offers')

schema_view = get_schema_view(
    openapi.Info(
        title="Cambio Express API",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path(config("DJANGO_ADMIN_URL", 'admin/'), admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include([
    	path('', include(router.urls)),
        path('auth/', include('authentication.urls')),
    ])),
    #path("", include("api.urls"))
]
