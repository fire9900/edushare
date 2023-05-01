from django.contrib import admin
from .models import Course, CourseTag


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags', 'get_teachers')
    filter_horizontal = ['related_teachers', 'tags']

    def get_teachers(self, obj):
        return '\n'.join([teacher.title for teacher in obj.related_teachers.all()])

    def get_tags(self, obj):
        return '\n'.join([tag.title for tag in obj.tags.all()])


@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = tuple(['title'])
    search_fields = tuple(['title'])
