from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from student import serializers
from student import models


class StudentAPIView(ListAPIView):
    queryset = models.Student.objects.all()
    # queryset = models.Student.objects.filter(passby='user1')  # directly applying filter value to queryset
    serializer_class = serializers.StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'name']

    #  overriding get_queryset()

    # def get_queryset(self):
    #     user = self.request.user  # current user
    #     return models.Student.objects.filter(passby=user)
