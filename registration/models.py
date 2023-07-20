from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    img = models.ImageField(default='default.jpg', upload_to='user_profile_images', verbose_name='Аватар')
    phone_number = models.IntegerField(null=True, verbose_name='Номер телефона')

    def __str__(self):
        return f'Профиль {self.user.username}'

    def save(self):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 500 or image.width > 500:
            resize = (500, 500)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профиля пользователей'
