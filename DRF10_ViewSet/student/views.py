from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from student import serializers
from student import models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# class StudentViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         print("******List******")
#         print("Basename: ", self.basename)
#         print("action: ", self.action)
#         print("detail: ", self.detail)
#         print("suffix: ", self.suffix)
#         print("name: ", self.name)
#         print("description: ", self.description)
#         student = models.Student.objects.all()
#         serializer = serializers.StudentSerializer(student, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         print("******Retrieve******")
#         print("Basename: ", self.basename)
#         print("action: ", self.action)
#         print("detail: ", self.detail)
#         print("suffix: ", self.suffix)
#         print("name: ", self.name)
#         print("description: ", self.description)
#         id = pk
#         if id is not None:
#             student = models.Student.objects.get(id=id)
#             serializer = serializers.StudentSerializer(student)
#             return Response(serializer.data)
#
#     def create(self, request):
#         print("******Create******")
#         print("Basename: ", self.basename)
#         print("action: ", self.action)
#         print("detail: ", self.detail)
#         print("suffix: ", self.suffix)
#         print("name: ", self.name)
#         print("description: ", self.description)
#         serializer = serializers.StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Student Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#         print("******Update******")
#         print("Basename: ", self.basename)
#         print("action: ", self.action)
#         print("detail: ", self.detail)
#         print("suffix: ", self.suffix)
#         print("name: ", self.name)
#         print("description: ", self.description)
#         id = pk
#         student = models.Student.objects.get(id=id)
#         serializer = serializers.StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Complete Student Data Updated'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def partial_update(self, request, pk=None):
#         print("******Partial Update******")
#         print("Basename: ", self.basename)
#         print("action: ", self.action)
#         print("detail: ", self.detail)
#         print("suffix: ", self.suffix)
#         print("name: ", self.name)
#         print("description: ", self.description)
#         id = pk
#         student = models.Student.objects.get(id=id)
#         serializer = serializers.StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Student Data Updated'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         print("******Destroy******")
#         print("Basename: ", self.basename)
#         print("action: ", self.action)
#         print("detail: ", self.detail)
#         print("suffix: ", self.suffix)
#         print("name: ", self.name)
#         print("description: ", self.description)
#         id = pk
#         student = models.Student.objects.get(id=id)
#         student.delete()
#         return Response({'msg': 'Student Deleted'}, status=status.HTTP_204_NO_CONTENT)
