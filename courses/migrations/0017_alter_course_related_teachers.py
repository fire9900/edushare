# Generated by Django 3.2.16 on 2023-05-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0025_auto_20230430_1249'),
        ('courses', '0016_auto_20230501_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='related_teachers',
            field=models.ManyToManyField(null=True, to='eduapp.Teacher', verbose_name='Связанные учителя'),
        ),
    ]
