# Generated by Django 3.2.16 on 2023-04-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0025_auto_20230430_1249'),
        ('courses', '0009_auto_20230430_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='related_teachers',
            field=models.ManyToManyField(to='eduapp.Teacher', verbose_name='Связанные учителя'),
        ),
        migrations.AddField(
            model_name='course',
            name='related_teachers',
            field=models.ManyToManyField(to='eduapp.Teacher', verbose_name='Связанные учителя'),
        ),
    ]
