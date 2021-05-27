import io

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from student.models import Student
from student.serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):

    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Student Created'}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Student Updated'}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        response = {'msg': 'Student Deleted'}
        return JsonResponse(response)


@csrf_exempt
def student(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Student Created'}
            # json_data = JSONRenderer().render(response)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(response)
        return JsonResponse(serializer.errors)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Student Updated'}
            return JsonResponse(response)
        return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        response = {'msg': 'Student Deleted'}
        return JsonResponse(response)
