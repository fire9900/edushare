# Generated by Django 3.2.16 on 2023-04-29 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0019_auto_20230430_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.CharField(max_length=50, verbose_name='Описание'),
        ),
    ]
