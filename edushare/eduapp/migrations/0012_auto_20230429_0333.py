# Generated by Django 3.2.16 on 2023-04-28 23:33

from django.db import migrations, models
import django.db.models.deletion
import eduapp.storage


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0011_auto_20230427_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Учителя на главной', 'verbose_name_plural': 'Учителя на главной'},
        ),
        migrations.AddField(
            model_name='gridsubject',
            name='bg_image_link',
            field=models.ImageField(null=True, storage=eduapp.storage.OverwriteStorage(), upload_to='images', verbose_name='Фоновое изображение'),
        ),
        migrations.AlterField(
            model_name='gridsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduapp.subject', verbose_name='Название предмета'),
        ),
    ]
