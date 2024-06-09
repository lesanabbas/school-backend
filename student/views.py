
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def index(request):
    # students = Student.objects.all()
    # return render(request, 'students/index.html', {'students': students})
    return JsonResponse({"ds":322})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_list(request):
    # students = Student.objects.filter(school=request.user.schooladmin.school)
    # serializer = StudentSerializer(students, many=True)
    # return Response(serializer.data)
    return JsonResponse({"ds":322})

