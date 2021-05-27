from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

from student.models import Student
from student.serializers import StudentSerializer


# Model object - Single Student Data
def student_detail(request, pk):
    """ Default content type is not set for HttpResponse,so we need set it explicitly """
    student = Student.objects.get(id=pk)  # Complex data type
    # print(student)
    serializer = StudentSerializer(student)  # Python native data type
    # print(serializer)
    # print(serializer.data)
    return JsonResponse(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)  # Json data
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')


# Query Set - All Student Data
def student_list(request):
    student = Student.objects.all()
    # print(student)
    serializer = StudentSerializer(student, many=True)
    # print(serializer)
    # print(serializer.data)
    return JsonResponse(serializer.data, safe=False)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
