from django.urls import path, include
from .views import user_views, feedback_views, me_views, account_views, common, graphs

urlpatterns = [
    path("users/", include([
        path("", user_views.UserList.as_view()),
        path("<int:id>/", user_views.UserDetails.as_view())
    ])),
    path("feedbacks/",include([
       path("", feedback_views.FeedbackList.as_view()),
       path("search/", feedback_views.search_feedbacks),
    ])),
    path("accounts/", include([
        path("", account_views.AccountList.as_view())
    ])),
    path("me/", me_views.MeDetails.as_view()),
    path("graphs/",include([
        path("get/<coin>",graphs.get)
    ])),
    path("getcsrf/", common.get_csrf),
]