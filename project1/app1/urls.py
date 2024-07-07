from django.urls import path, include

from app1.views import Anime1, Anime_item

urlpatterns = [
    path("anime/",Anime1.as_view()),
    path("anime/<int:pk>/",Anime_item.as_view())
]