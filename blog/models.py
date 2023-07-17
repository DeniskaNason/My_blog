from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя')
    slug = models.SlugField(default='', null=False, verbose_name='SLUG')

    def __str__(self):
        return f'Модель "Tag" с именем "{self.name}"'

    def get_url(self):
        return reverse('tag-detail', args=[self.slug])

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Содержание')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    rating = models.PositiveIntegerField(default=1, verbose_name='Рейтинг')
    slug = models.SlugField(default='', null=False, verbose_name='SLUG')
    publication_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'Модель "Post" с именем "{self.name}"'

    def get_url(self):
        return reverse('post-detail', args=[self.slug])

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
