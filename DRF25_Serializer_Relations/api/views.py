from rest_framework import viewsets

from api import serializers
from api import models


class SongViewSet(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = models.Singer.objects.all()
    serializer_class = serializers.SingerSerializer
