from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from courseApp.models import Course
from courseApp.serializers import CourseSerializer
from rest_framework import generics, mixins


class CourseList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        # From ListModelMixin
        return self.list(request)

    def post(self, request):
        # From CreateModelMixin
        return self.create(request)


class CourseDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        # From RetrieveModelMixin
        return self.retrieve(request, pk)

    def update(self, request, pk):
        # From UpdateModelMixin
        return self.update(request, pk)

    def remove(self, request, pk):
        # From DestroyModelMixin
        return self.destroy(request, pk)

"""
class CourseList(APIView):

    def get(self, request):
        courses = Course.objects.all()
        courses_serializer = CourseSerializer(courses, many=True)
        return Response(courses_serializer.data)

    def post(self, request):
        courses_serializer = CourseSerializer(data=request.data)
        if courses_serializer.is_valid():
            courses_serializer.save()
            return Response(courses_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(courses_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetails(APIView):

    def get_object(self, pk):
        try:
            course = Course.objects.get(pk=pk)
            return course
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        course_serializer = CourseSerializer(course)
        return Response(course_serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        course_serializer = CourseSerializer(course, data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        else:
            return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""