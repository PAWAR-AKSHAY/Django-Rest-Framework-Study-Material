from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, DestroyModelMixin

from student import models
from student import serializers


# List and Create - PK not required
class StudentCreateList(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieveUpdateDelete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self. update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self. update(request, *args, **kwargs)
#
#
# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
