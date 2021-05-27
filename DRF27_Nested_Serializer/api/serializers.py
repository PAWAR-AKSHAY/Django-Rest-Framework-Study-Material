from rest_framework import serializers

from api import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many=True, read_only=True)  # Nested Serializer

    class Meta:
        model = models.Singer
        fields = ['id', 'name', 'gender', 'sungby']
