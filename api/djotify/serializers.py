from rest_framework import serializers
from .models import (
    Artist,
    Song,
    Album,
    Genre,
    Playlist,
    Keyword,
    PlaylistSong,
    SongArtist,
    PlaylistKeyword
)
from .fields import *


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumListingField(many=True, queryset=Album.objects.all(), required=False)
    class Meta:
        model = Artist
        fields = ["id", "name", "listeners", "biography", "albums",]


class GenreSerializer(serializers.ModelSerializer):
    songs = SongListingField(many=True, queryset=Song.objects.all(), required=False)
    class Meta:
        model = Genre
        fields = ["id", "name", "songs",]


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["id", "title",]


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistListingField(read_only=True, required=False)
    songs = SongListingField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ["id", "title", "artist", "year_released", "songs",]

    # def create(self, validated_data):
    #     artist = validated_data.pop('artist')
    #     obj, created = Artist.objects.get(name=artist['name'])
    #     album = Album.objects.create(**validated_data, artist=obj)
    #     return album


class SongSerializer(serializers.ModelSerializer):
    album = AlbumListingField(queryset=Album.objects.all())
    genre = GenreListingField(queryset=Genre.objects.all())
    class Meta:
        model = Song
        fields = ["id", "title", "length", "explicit", "plays", "album", "genre",]
    
    # def create(self, validated_data):
    #     album = validated_data.pop('album')
    #     genre = validated_data.pop('genre')
    #     obj_album, created_album = Album.objects.get_or_create(title=album['title'])
    #     obj_genre, created_genre = Genre.objects.get_or_create(name=genre['name'])
    #     song = Song.objects.create(**validated_data, album=obj_album, genre=obj_genre)
    #     return song


class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongListingField(many=True, queryset=Song.objects.all(), required=False)
    class Meta:
        model = Playlist
        fields = ["id", "title", "songs"]

    # def create(self, validated_data):
    #     song = validated_data.pop('song')
    #     obj, created = Song.objects.get_or_create(title=song['title'])
    #     playlist = Playlist.objects.create(**validated_data, song=obj)
    #     return playlist


class PlaylistSongSerializer(serializers.ModelSerializer):
    songs = SongListingField(many=True, queryset=Song.objects.all(), required=False)
    playlists = PlaylistListingField(queryset=Playlist.objects.all(), required=False)
    class Meta:
        model = PlaylistSong
        fields = "__all__"


class PlaylistKeywordSerializer(serializers.ModelSerializer):
    playlists = PlaylistListingField(queryset=Playlist.objects.all(), required=False)
    keywords = KeywordListingField(queryset=Playlist.objects.all(), required=False)
    class Meta:
        model = PlaylistKeyword
        fields = "__all__"
