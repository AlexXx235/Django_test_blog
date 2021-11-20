from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
