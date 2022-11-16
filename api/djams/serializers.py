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


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    genre = GenreSerializer()
    class Meta:
        model = Song
        fields = "__all__"
    
    def create(self, validated_data):
        album = validated_data.pop('category')
        genre = validated_data.pop('genre')
        obj, created = Album.objects.get_or_create(title=album['title'])
        obj2, created2 = Genre.objects.get_or_create(name=genre['name'])
        song = Song.objects.create(**validated_data, album=obj, genre=obj2)
        return song

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Album
        fields = "__all__"

    def create(self, validated_data):
        artist = validated_data.pop('artist')
        obj, created = Artist.objects.get_or_create(name=artist['name'])
        album = Album.objects.create(**validated_data, artist=obj)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    song = SongSerializer()
    class Meta:
        model = Playlist
        fields = "__all__"

    def create(self, validated_data):
        song = validated_data.pop('song')
        obj, created = Song.objects.get_or_create(title=song['title'])
        playlist = Playlist.objects.create(**validated_data, song=obj)
