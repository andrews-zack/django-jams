from django.urls import path, include
from .views import (
    ArtistViewSet,
    SongViewSet,
    AlbumViewSet,
    GenreViewSet,
    PlaylistViewSet,
    KeywordViewSet,
    PlaylistSongViewSet,
    PlaylistKeywordViewSet
)
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'songs', SongViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'keywords', KeywordViewSet)
router.register(r'playlists_songs', PlaylistSongViewSet)
router.register(r'playlists_keywords', PlaylistKeywordViewSet)

urlpatterns = [
    path('', include(router.urls))
]