from rest_framework import serializers
from .models import (
    Artist,
    Album,
    Lyric,
    Song
)

class AlbumSerializers(serializers.ModelSerializer):
    
    artist = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Album
        fields = ["id", "artist", "name", "released", "cover"]


class ArtistSerializers(serializers.ModelSerializer):
    
    albums = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Artist
        fields = ["id", "first_name", "last_name", "artist_pic", "num_stars", "albums"]

class LyricSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Lyric
        fields = ["id", "title"]

class SongSerializers(serializers.ModelSerializer):
    
    artist = serializers.StringRelatedField()
    album = serializers.StringRelatedField()
    lyric = serializers.SlugRelatedField(
        read_only=True,
        slug_field='content'
     )
    
    class Meta:
        model = Song
        fields = ["id", "name", "released", "artist", "album", "lyric"]