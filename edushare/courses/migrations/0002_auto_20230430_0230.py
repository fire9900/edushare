# Generated by Django 3.2.16 on 2023-04-29 22:30

from django.db import migrations, models
import eduapp.storage
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0020_alter_teacher_description'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='bg_image',
            field=optimized_image.fields.OptimizedImageField(null=True, storage=eduapp.storage.OverwriteStorage(), upload_to='course_bgimages', verbose_name='Фоновое изображение'),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='Опсание', verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='course',
            name='related_teachers',
            field=models.ManyToManyField(to='eduapp.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_photo_visible',
            field=models.BooleanField(default=True, verbose_name='Отображать фото учителя'),
        ),
    ]
