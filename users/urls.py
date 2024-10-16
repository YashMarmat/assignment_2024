from django.urls import path
from .views import (
    UsersApiView, 
    StudentsListCreateAPIView, 
    StudentDetailAPIView, 
    CourseListCreateAPIView, 
    CourseDetailAPIView,
    DepartmentListCreateAPIView,
    DepartmentDetailAPIView,
    AttendanceListCreateAPIView,
    AttendanceDetailAPIView,
)


urlpatterns = [
    path('users/', UsersApiView.as_view(), name='users'),
    path('students/', StudentsListCreateAPIView.as_view(), name="students"),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name="student_detail"),
    path('courses/', CourseListCreateAPIView.as_view(), name="courses"),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name="course_detail"),
    path('attendances/', AttendanceListCreateAPIView.as_view(), name="attendances"),
    path('attendances/<int:pk>/', AttendanceDetailAPIView.as_view(), name="attendance_detail"),
    path('departments/', DepartmentListCreateAPIView.as_view(), name="departments"),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name="department_detail"),
]