from django.db import models
from colorfield.fields import ColorField
from .storage import OverwriteStorage
from optimized_image.fields import OptimizedImageField


class Subject(models.Model):
    subject_name = models.CharField(verbose_name='Название предмета', max_length=50)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = 'Название предмета'
        verbose_name_plural = 'Названия предметов'


class GridSubject(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Название предмета', on_delete=models.CASCADE)
    on_index = models.BooleanField(verbose_name='Отображать на главной', default=True)
    bg_text_color = ColorField(verbose_name='Цвет фона текста', default='#5FAFDC')
    bg_image = OptimizedImageField(verbose_name='Фоновое изображение', upload_to='images',
                                   storage=OverwriteStorage())

    def __str__(self):
        return self.subject.subject_name

    class Meta:
        verbose_name = 'Предмет на главной'
        verbose_name_plural = 'Предметы на главной'


class Teacher(models.Model):
    title = models.CharField(verbose_name='ФИО', max_length=50)
    description = models.CharField(verbose_name='Описание', max_length=50)
    photo = OptimizedImageField(verbose_name='Фото', upload_to='teachers',
                                storage=OverwriteStorage())
    on_index = models.BooleanField(verbose_name='Отображать на главной', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'
