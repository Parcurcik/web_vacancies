from django.db import models


class Navigation(models.Model):
    title = models.FileField(upload_to='photos/%Y/%m/%d', blank = False, verbose_name='Заголовок в SVG формате')
    logo_field = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, verbose_name='Логотип')
    first_menu = models.TextField(blank=False, verbose_name='Первый пункт меню', max_length=25)
    second_menu = models.TextField(blank=False, verbose_name='Второй пункт меню', max_length=25)
    thierd_menu = models.TextField(blank=False, verbose_name='Третий пункт меню', max_length=25)
    fourth_menu = models.TextField(blank=False, verbose_name='Четвертый пункт меню',max_length=25)
    fifth_menu = models.TextField(blank=False, verbose_name='Пятый пункт меню', max_length=25)
    all_rights = models.TextField(blank=False, verbose_name='Организация', max_length=255)
    author = models.TextField(blank=False, verbose_name='Автор', max_length=50)

class MainPageInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок страницы')
    content = models.TextField(blank=True, verbose_name='Описание профессии')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, verbose_name='Фото')
    photo_description = models.TextField(blank=True, verbose_name='Описание фото')

class Demand(models.Model):
    main_title = models.CharField(max_length=255, blank=True, verbose_name='Заголовок страницы')
    first_title = models.CharField(max_length=255,blank=True, verbose_name='Заголовок блока')
    first_content = models.TextField(blank=True, verbose_name='Табличка для первого блока')
    first_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, verbose_name='Первое фото')
    second_title = models.CharField(max_length=255, blank=True,  verbose_name='Заголовок второго блока')
    second_content = models.TextField(blank=True,  verbose_name='Табличка для второго блока')
    second_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, verbose_name='Второе фото')

class Geography(models.Model):
    main_title = models.CharField(max_length=255, blank=True, verbose_name='Заголовок страницы')
    first_title = models.CharField(max_length=255,blank=True, verbose_name='Заголовок первого блока')
    first_content = models.TextField(blank=True, verbose_name='Табличка для первого блока')
    second_title = models.CharField(max_length=255,blank=True, verbose_name='Заголовок второго блока')
    second_content = models.TextField(blank=True, verbose_name='Табличка для второго блока')
    second_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, verbose_name='Фото')




