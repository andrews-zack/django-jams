from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Artist(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    listeners = models.IntegerField(null=False, blank=False)
    biography = models.TextField()          # Look up params
    image = models.URLField()           # Look up params
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Song(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    length = models.FloatField(null=False, blank=False)
    explicit = models.BooleanField(null=False, blank=False)         # Look up params
    plays = models.IntegerField(null=False, blank=False)
    album = models.ForeignKey("Album", on_delete=models.PROTECT)
    genre = models.ForeignKey("Genre", on_delete=models.PROTECT)
    # playlists = models.ManyToManyField("Playlist")
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()         # Look up params

class Album(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    year_released = models.DateField(null=False, blank=False)     # Look up params
    is_original = models.BooleanField(null=False, blank=False)
    artist = models.ForeignKey("Artist", on_delete=models.PROTECT)
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()

class Playlist(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()

class Keyword(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()

class PlaylistSong(models.Model):
    song = models.ForeignKey("Song", on_delete=models.PROTECT)
    playlist = models.ForeignKey("Playlist", on_delete=models.PROTECT)
    track_num = models.PositiveIntegerField()

class SongArtist(models.Model):
    artist = models.ForeignKey("Artist", on_delete=models.PROTECT)
    song = models.ForeignKey("Song", on_delete=models.PROTECT)

class PlaylistKeyword(models.Model):
    playlist = models.ForeignKey("Playlist", on_delete=models.PROTECT)
    keyword = models.ForeignKey("Keyword", on_delete=models.PROTECT)

