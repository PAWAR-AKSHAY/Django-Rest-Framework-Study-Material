from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from student import models
from student import serializers


class StudentAPIView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            student = models.Student.objects.get(id=id)
            serializer = serializers.StudentSerializer(student)
            return Response(serializer.data)

        student = models.Student.objects.all()
        serializer = serializers.StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        student = models.Student.objects.get(id=id)
        serializer = serializers.StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Student Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        student = models.Student.objects.get(id=id)
        serializer = serializers.StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Student Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        student = models.Student.objects.get(id=id)
        student.delete()
        return Response({'msg': 'Student Deleted'})
