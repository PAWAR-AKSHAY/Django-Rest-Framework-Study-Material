from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from student import models
from student import serializers


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            student = models.Student.objects.get(id=id)
            serializer = serializers.StudentSerializer(student)
            return Response(serializer.data)

        student = models.Student.objects.all()
        serializer = serializers.StudentSerializer(student, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        student = models.Student.objects.get(id=id)
        serializer = serializers.StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Student Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        student = models.Student.objects.get(id=id)
        serializer = serializers.StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Student Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        student = models.Student.objects.get(id=id)
        student.delete()
        return Response({'msg': 'Student Deleted'})
