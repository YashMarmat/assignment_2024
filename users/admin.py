from django.contrib import admin
from .models import CustomUser, Student, Course, Department, AttendanceLog


admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(AttendanceLog)