# Generated by Django 3.2.16 on 2023-04-30 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_course_related_teachers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseTeachers',
        ),
    ]
