# Generated by Django 3.2.16 on 2023-04-27 13:17

from django.db import migrations, models
import eduapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0005_alter_gridsubject_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gridsubject',
            name='bg_image',
            field=models.FileField(upload_to='media/', verbose_name='Фоновое изображение'),
        ),
    ]
