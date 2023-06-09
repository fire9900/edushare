# Generated by Django 3.2.16 on 2023-04-29 00:06

from django.db import migrations
import eduapp.storage
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0015_rename_bg_image_link_gridsubject_bg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gridsubject',
            name='bg_image',
            field=optimized_image.fields.OptimizedImageField(null=True, storage=eduapp.storage.OverwriteStorage(), upload_to='images', verbose_name='Фоновое изображение'),
        ),
    ]
