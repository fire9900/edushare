# Generated by Django 3.2.16 on 2023-04-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0009_auto_20230427_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
