from studentApp.models import Student
from studentApp.serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)

    def post(self, request):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)