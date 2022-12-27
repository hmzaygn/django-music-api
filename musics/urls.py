from django.urls import path, include
from .views import (
    ArtistView,
    AlbumView,
    LyricView,
    SongView
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("artist", ArtistView)
router.register("album", AlbumView)
router.register("lyric", LyricView)
router.register("song", SongView)

urlpatterns = [
    path("", include(router.urls))
]

# urlpatterns += router.urls