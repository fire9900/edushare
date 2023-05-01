from django.contrib import admin
from colorfield.fields import ColorField
from .models import Subject, GridSubject, Teacher

admin.site.register(Subject)


@admin.action(description="Включить отображение на главной")
def on_index_visible(modeladmin, request, queryset):
    queryset.update(on_index=True)


@admin.action(description="Выключить отображение на главной")
def on_index_notvisible(modeladmin, request, queryset):
    queryset.update(on_index=False)


@admin.register(GridSubject)
class GridSubjectAdmin(admin.ModelAdmin):
    bg_text_color = ColorField()
    list_display = ('id', 'subject', 'on_index')
    search_fields = ('id', 'subject__subject_name')
    actions = [on_index_visible, on_index_notvisible]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'on_index')
    search_fields = ('title', 'description')
    actions = [on_index_visible, on_index_notvisible]
