from rest_framework import serializers

from api import models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['id', 'title', 'duration', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = models.Singer
        fields = ['id', 'name', 'gender', 'song']
