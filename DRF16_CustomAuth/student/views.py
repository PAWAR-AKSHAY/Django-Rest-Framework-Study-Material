from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from student import serializers
from student import models
from student.customauth import CustomAuthentication


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
