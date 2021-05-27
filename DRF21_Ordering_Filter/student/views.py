from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from student import serializers
from student import models


class StudentAPIView(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    ordering_fields = ['name', 'city']
