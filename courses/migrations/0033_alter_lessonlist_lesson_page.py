# Generated by Django 4.2.6 on 2025-01-16 01:37

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0032_lessonlist_lesson_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonlist',
            name='lesson_page',
            field=markdownx.models.MarkdownxField(null=True),
        ),
    ]
