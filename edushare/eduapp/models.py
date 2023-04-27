from django.db import models
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
import xml.etree.cElementTree as et
from .storage import OverwriteStorage


def is_svg(file):
    tag = None
    f = file.file.open("r")
    try:
        for event, el in et.iterparse(f, ('start',)):
            tag = el.tag
            break
    except et.ParseError:
        pass
    return tag == '{http://www.w3.org/2000/svg}svg'


def validate_svg(file):
    try:
        if is_svg(file):
            return file
        if validate_image_file_extension(file):
            return file
    except Exception as err:
        raise ValidationError("Данное расширение файла не поддерживется. Разрешенные расширения: blp, bmp, dib, bufr, cur, pcx, dcx, dds, ps, eps, fit, fits, fli, flc, ftc, ftu, gbr, gif, grib, h5, hdf, png, apng, jp2, j2k, jpc, jpf, jpx, j2c, icns, ico, im, iim, jfif, jpe, jpg, jpeg, mpg, mpeg, tif, tiff, mpo, msp, palm, pcd, pdf, pxr, pbm, pgm, ppm, pnm, psd, qoi, bw, rgb, rgba, sgi, svg, ras, tga, icb, vda, vst, webp, wmf, emf, xbm, xpm.")


class Subject(models.Model):
    subject_name = models.CharField(verbose_name='Название предмета', max_length=50)

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = 'Название предмета'
        verbose_name_plural = 'Названия предметов'


class GridSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    bg_image = models.FileField(verbose_name='Фоновое изображение', upload_to='images', validators=[validate_svg], storage=OverwriteStorage())
    bg_text_color = ColorField(verbose_name='Цвет фона текста', default='#5FAFDC')

    def __str__(self):
        return self.subject.subject_name

    class Meta:
        verbose_name = 'Предмет на главной'
        verbose_name_plural = 'Предметы на главной'


class Teacher(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=50)
    description = models.TextField(verbose_name='Описание', max_length=50)
    photo = models.ImageField(verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'