from django.db import models
from django.urls import reverse
from eduapp.models import Subject, Teacher
from eduapp.storage import OverwriteStorage
from optimized_image.fields import OptimizedImageField
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from colorfield.fields import ColorField
from django.shortcuts import reverse


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class CourseTag(models.Model):
    title = models.CharField(verbose_name='Тэг', max_length=50)
    color = ColorField(default='#2C3E50')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Course(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=100)
    tags = models.ManyToManyField(CourseTag, verbose_name='Тэги')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    related_teachers = models.ManyToManyField(Teacher, verbose_name='Связанные учителя')
    description = models.TextField(verbose_name='Описание', default='Описание')
    bg_image = OptimizedImageField(verbose_name='Фоновое изображение', upload_to='course_bgimages',
                                   storage=OverwriteStorage(), blank=True, null=True)
    teacher_photo_visible = models.BooleanField(verbose_name='Отображать фото учителя', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'


pre_save.connect(slug_generator, sender=Course)
