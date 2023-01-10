# Generated by Django 4.1.4 on 2023-01-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок страницы')),
                ('first_title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок первого блока')),
                ('first_content', models.TextField(blank=True, verbose_name='Табличка для первого блока')),
                ('second_title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок второго блока')),
                ('second_content', models.TextField(blank=True, verbose_name='Табличка для второго блока')),
                ('second_photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
            ],
        ),
        migrations.AlterField(
            model_name='demand',
            name='first_content',
            field=models.TextField(blank=True, verbose_name='Табличка для первого блока'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='first_photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Первое фото'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='first_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок блока'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='second_content',
            field=models.TextField(blank=True, verbose_name='Табличка для второго блока'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='second_photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Второе фото'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='second_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Заголовок второго блока'),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='all_rights',
            field=models.TextField(max_length=255, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='author',
            field=models.TextField(max_length=50, verbose_name='Автор'),
        ),
    ]
