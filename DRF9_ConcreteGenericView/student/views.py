from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,\
    DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView

from student import models
from student import serializers


# class StudentList(ListAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#
# class StudentCreate(CreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#
# class StudentRetrieve(RetrieveAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#
# class StudentUpdate(UpdateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#
# class StudentDestroy(DestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#
# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer


class StudentListCreate(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
