# Generated by Django 3.2.16 on 2023-04-27 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GridSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(verbose_name='Активен?')),
                ('bg_image', models.ImageField(upload_to='', verbose_name='Фоновое изображение')),
                ('bg_text_color', models.BinaryField(verbose_name='Цвет фона текста')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.subject')),
            ],
        ),
    ]
