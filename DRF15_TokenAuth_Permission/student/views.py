from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from student import serializers
from student import models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Only Authenticated users have access
    # permission_classes = [IsAuthenticatedOrReadOnly]
