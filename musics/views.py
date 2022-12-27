from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import (
    Artist,
    Album,
    Lyric,
    Song
)
from .serializers import (
    ArtistSerializers,
    AlbumSerializers,
    LyricSerializers,
    SongSerializers
)

class ArtistView(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers

class AlbumView(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

class LyricView(ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializers

class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers