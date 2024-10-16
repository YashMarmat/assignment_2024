from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser, Student, Course, Department, AttendanceLog
from .serializers import UserSerializer, StudentSerializer, CourseSerializer, DepartmentSerializer, AttendanceLogSerializer


class UsersApiView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class StudentsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer


class AttendanceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer