from rest_framework import serializers
from .models import CustomUser, Student, Course, Department, AttendanceLog


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "type", "full_name", "username", "email", "submitted_by", "updated_at"]


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class AttendanceLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceLog
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"