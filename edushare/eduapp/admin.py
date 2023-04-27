from django.contrib import admin
from colorfield.fields import ColorField
from .models import Subject, GridSubject, Teacher

admin.site.register(Subject)


@admin.register(GridSubject)
class GridSubjectAdmin(admin.ModelAdmin):
    bg_text_color = ColorField()


admin.site.register(Teacher)
