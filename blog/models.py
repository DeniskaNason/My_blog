from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


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
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор статьи')

    def __str__(self):
        return f'Модель "Post" с именем "{self.name}"'

    def get_url(self):
        return reverse('post-detail', args=[self.slug])

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
