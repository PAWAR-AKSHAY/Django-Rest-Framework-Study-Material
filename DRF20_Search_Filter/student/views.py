from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from student import serializers
from student import models


class StudentAPIView(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['city']
    # search_fields = ['name, 'city']
    # search_fields = ['^name']
