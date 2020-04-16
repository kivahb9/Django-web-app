from django.urls import path
from . import views
from .views import (
    challenges_detail_view,
    challenges_list_view,
    download,
    UploadProjectCreateView,
    RankingListView,
    register,
)
from .models import Challenges
from django.conf.urls.static import static
from django.conf import settings
import os

app_name = "cha"

urlpatterns = [
    path(
        "challenges_view/<int:id>", views.challenges_detail_view, name="challenges_view"
    ),
    path("challenge/", views.challenges_list_view, name="challenge"),
    path("(?P<challenge.challenge_path>.*)$/", views.download, name="challenges_view"),
    path(
        "uploadproject/<int:id>",
        UploadProjectCreateView.as_view(),
        name="uploadproject",
    ),
    path("result/", RankingListView.as_view(), name="result"),
    path("challenges_view1/<int:id>", views.register, name="challenges_view1"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
