from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle

from student import serializers
from student import models
from student.throttling import CustomRateThrottle


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Default Throttle rates are applied
    throttle_classes = [AnonRateThrottle, CustomRateThrottle]  # Custom Throttle rates are applied


# class StudentList(ListAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstudent'
#
#
# class StudentCreate(CreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'poststudent'
#
#
# class StudentRetrieve(RetrieveAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstudent'
#
#
# class StudentUpdate(UpdateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystudent'
#
#
# class StudentDestroy(DestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'modifystudent'
