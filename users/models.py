from django.db import models
from django.contrib.auth.models import AbstractUser


class CommonInfo(models.Model):
    submitted_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser, CommonInfo):
    type = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=200, blank=True)
    submitted_by = models.CharField(max_length=120, blank=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"


class Department(CommonInfo):
    department_name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.department_name}"

class Student(CommonInfo):
    full_name = models.CharField(max_length=120)
    department = models.ForeignKey(to=Department, related_name='department', on_delete=models.CASCADE)
    student_class = models.IntegerField(verbose_name="class")
    
    def __str__(self):
        return f"{self.full_name}"

class Course(CommonInfo):
    course_name = models.CharField(max_length=120)
    department = models.ForeignKey(to=Department, related_name='course', on_delete=models.CASCADE)
    semester = models.IntegerField()
    course_class = models.IntegerField(verbose_name="class")
    lecture_hours = models.IntegerField()
    
    def __str__(self):
        return f"{self.course_name}"

class AttendanceLog(CommonInfo):
    student = models.ForeignKey(to=Student, related_name="attendance", on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, related_name="course_backref", on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.full_name} | Present: {self.present}"
    