from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser, Student, Course, Department, AttendanceLog
from .serializers import UserSerializer, StudentSerializer, CourseSerializer, DepartmentSerializer, AttendanceLogSerializer


class UsersApiView(generics.ListAPIView):
    """List all users"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class StudentsListCreateAPIView(generics.ListCreateAPIView):
    """List and Create Students API"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Edit and Delete Students API"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseListCreateAPIView(generics.ListCreateAPIView):
    """List and Create Courses API"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Edit and Delete Courses API"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    """List and Create Department API"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Edit and Delete Department API"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    """List and Create Attendance API"""
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer


class AttendanceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Edit and Delete Attendance API"""
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceLogSerializer