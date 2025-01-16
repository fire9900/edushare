from django.db import models
from eduapp.models import Teacher
from eduapp.storage import OverwriteStorage
from optimized_image.fields import OptimizedImageField
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from colorfield.fields import ColorField
from django.shortcuts import reverse
from django.db.models.functions import Length
from mptt.models import MPTTModel, TreeForeignKey
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class CourseTag(models.Model):
    title = models.CharField(verbose_name='Имя тэга', max_length=50, unique=True)
    color = ColorField(default='#2C3E50')
    order_by = models.IntegerField(verbose_name='Приоритет', default=1)

    title.register_lookup(Length)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['order_by', 'title__length', 'title']


class Course(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=100, unique=True)
    tags = models.ManyToManyField(CourseTag, verbose_name='Тэги')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    related_teachers = models.ManyToManyField(Teacher, verbose_name='Связанные учителя', blank=True)
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


class LessonList(MPTTModel):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children', verbose_name='Родитель')
    related_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True,
                                       verbose_name='Связанный курс')
    order_by = models.IntegerField(verbose_name='Приоритет', default=1)
    lesson_page = MarkdownxField(null=True, blank=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['related_course', 'order_by', 'title']

    @property
    def formatted_markdown(self):
        return markdownify(self.lesson_page)

    class Meta:
        verbose_name = 'Список уроков'
        verbose_name_plural = 'Список уроков'

    def get_absolute_url(self):
        return reverse('lesson', kwargs={'id': self.related_course.pk, 'slug': self.slug})


pre_save.connect(slug_generator, sender=LessonList)
