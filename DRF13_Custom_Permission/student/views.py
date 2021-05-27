from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from student import serializers
from student import models
from student.permissions import StudentPermission


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [StudentPermission]
