# Generated by Django 3.2.16 on 2023-04-30 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0024_delete_teacherwithdescription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Учителя', 'verbose_name_plural': 'Учителя'},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='title',
        ),
    ]
