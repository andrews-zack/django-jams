from django.shortcuts import render
from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet
from .models import (
    Artist,
    Song,
    Album,
    Genre,
    Playlist,
    Keyword,
    PlaylistSong,
    PlaylistKeyword
)
from .serializers import (
    ArtistSerializer,
    SongSerializer,
    AlbumSerializer,
    GenreSerializer,
    PlaylistSerializer,
    KeywordSerializer,
    PlaylistSongSerializer,
    PlaylistKeywordSerializer
)
from rest_framework.response import Response
from rest_framework import filters


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['plays', 'length']


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class KeywordViewSet(ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class PlaylistSongViewSet(ModelViewSet):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class PlaylistKeywordViewSet(ModelViewSet):
    queryset = PlaylistKeyword.objects.all()
    serializer_class = PlaylistKeywordSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
