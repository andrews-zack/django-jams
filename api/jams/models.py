from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    listeners = models.IntegerField(null=False)
    biography = models.TextField()          # Look up params
    image = models.URLField()           # Look up params
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Song(models.Model):
    title = models.CharField(max_length=100, null=False)
    length = models.FloatField(null=False)
    explicit = models.BooleanField(null=False)         # Look up params
    plays = models.IntegerField(null=False)
    album = models.ForeignKey("Album", on_delete=models.PROTECT)
    genre = models.ForeignKey("Genre", on_delete=models.PROTECT)
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()         # Look up params

class Album(models.Model):
    title = models.CharField(max_length=50, null=False)
    year_released = models.DateField(null=False)     # Look up params
    is_original = models.BooleanField(null=False)
    artist = models.ForeignKey("Artist", on_delete=models.PROTECT)
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField()         # Look up params
    updated_at = models.DateTimeField()

