# Generated by Django 3.2.16 on 2023-04-28 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0014_remove_gridsubject_bg_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gridsubject',
            old_name='bg_image_link',
            new_name='bg_image',
        ),
    ]