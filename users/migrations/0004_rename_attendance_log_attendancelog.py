# Generated by Django 4.2.11 on 2024-10-16 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_department_id_course_department'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendance_log',
            new_name='AttendanceLog',
        ),
    ]
