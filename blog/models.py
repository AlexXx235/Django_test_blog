from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
