from rest_framework import serializers
from student import models


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'url', 'name', 'roll', 'city']  # we get url by default because of HyperlinkedModelSerializer
