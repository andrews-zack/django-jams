from rest_framework import serializers
from .models import *

class SongListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    # def to_internal_value(self, data):
    #     return Song.objects.get(name=data)


class ArtistListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return Artist.objects.get(name=data)


class AlbumListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return Album.objects.get(title=data)


class GenreListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return Genre.objects.get(name=data)