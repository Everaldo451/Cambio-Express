from django.urls import path, include
from .views import last_five_offerts

urlpatterns = [
    path("last-five/<coin>/<index_var>", last_five_offerts)
]
