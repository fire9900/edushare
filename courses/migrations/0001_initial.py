# Generated by Django 3.2.16 on 2023-04-29 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eduapp', '0018_auto_20230430_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.subject', verbose_name='Название предмета')),
            ],
        ),
    ]
