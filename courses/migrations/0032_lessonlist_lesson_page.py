# Generated by Django 4.2.6 on 2025-01-15 21:52

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0031_lessonlist_order_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonlist',
            name='lesson_page',
            field=markdownx.models.MarkdownxField(default=''),
            preserve_default=False,
        ),
    ]
