# Generated by Django 3.2.16 on 2023-04-29 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0018_auto_20230430_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gridsubject',
            name='is_active',
        ),
        migrations.AddField(
            model_name='gridsubject',
            name='on_index',
            field=models.BooleanField(default=True, verbose_name='Отображать на главной'),
        ),
    ]
