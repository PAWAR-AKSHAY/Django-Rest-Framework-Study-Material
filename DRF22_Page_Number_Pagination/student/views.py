from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from student import serializers
from student import paginations
from student import models


class StudentAPIView(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    pagination_class = paginations.CustomPagination
