from django.test import TestCase, Client
from .models import Student, Department, Course
from django.urls import reverse


class StudentAPITest(TestCase):

    def setUp(self):

        # setting up
        self.department = Department.objects.create(
            department_name='CSE',
            submitted_by='Yash'
        )

        self.student = Student.objects.create(
            full_name = 'Sam',
            department = self.department,
            student_class = 9
        )

        self.course = Course.objects.create(
            course_name = 'Django',
            department = self.department,
            semester = 2,
            course_class = 8,
            lecture_hours = 3
        )

    def test_departments_api(self):
        response = self.client.get("/api/departments/")
        self.assertEqual(response.status_code, 200)

    def test_department_values(self):
        response = self.client.get(reverse("departments"))
        self.assertEqual(f"{self.department.department_name}", "CSE")
        self.assertEqual(response.status_code, 200)

    def test_students_api(self):
        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, 200)

    def test_students_values(self):
        response = self.client.get(reverse("students"))
        self.assertEqual(f"{self.student.full_name}", "Sam")
        self.assertEqual(response.status_code, 200)

    def test_course_api(self):
        response = self.client.get("/api/courses/")
        self.assertEqual(response.status_code, 200)

    def test_course_values(self):
        response = self.client.get(reverse("courses"))
        self.assertEqual(f"{self.course.course_name}", "Django")
        self.assertEqual(response.status_code, 200)


    # And similarly many other test cases can be added, left it to save time.