from django.db import models

class MainPageInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название профессии')
    content = models.TextField(blank=True, verbose_name='Описание профессии')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, verbose_name='Фото')


