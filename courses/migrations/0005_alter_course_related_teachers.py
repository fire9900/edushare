# Generated by Django 3.2.16 on 2023-04-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0023_teacherwithdescription'),
        ('courses', '0004_alter_course_related_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='related_teachers',
            field=models.ManyToManyField(to='eduapp.TeacherWithDescription'),
        ),
    ]