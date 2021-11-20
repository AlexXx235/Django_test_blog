from django.db import models
from django.urls import reverse, reverse_lazy
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'article_id': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
