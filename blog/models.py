from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Модель Tag с именем {self.name}'

    def get_url(self):
        return reverse('', args=[self.name])


class Post(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    rating = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'Модель Post с именем {self.name}'

    def get_url(self):
        return reverse('post-detail', args=[self.slug])
