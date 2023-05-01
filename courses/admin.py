from django.contrib import admin
from .models import Course, CourseTag, LessonList
from mptt.admin import MPTTModelAdmin


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags', 'get_teachers')
    filter_horizontal = ['related_teachers', 'tags']

    @admin.display(description='Учителя')
    def get_teachers(self, obj):
        return '\n'.join([teacher.title for teacher in obj.related_teachers.all()])

    @admin.display(description='Тэги')
    def get_tags(self, obj):
        return '\n'.join([tag.title for tag in obj.tags.all()])


@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_by')
    search_fields = tuple(['title'])


@admin.register(LessonList)
class LessonListAdmin(MPTTModelAdmin):
    list_display = ('title', 'related_course', 'order_by')
    search_fields = ('title', 'related_course')