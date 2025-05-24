from django.urls import path, include
from .views import graphs, swagger

urlpatterns = [
    path("users/", include("users.urls")),
    path("feedbacks/",include("feedbacks.urls")),
    path("accounts/", include("accounts.urls")),
    path("me/", include("me.urls")),
    path("offerts/", include("offerts.urls")),
    path("auth/", include("authentication.urls")),
    path("graphs/",include([
        path("get/<coin>",graphs.get)
    ])),
    path("swagger-ui/", swagger.schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui")
]