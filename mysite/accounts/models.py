from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Модель профиля пользователя"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', verbose_name='Аватар')
    bio = models.TextField(verbose_name='Информация о пользователе')

    class Meta:
        ordering = ['user']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username
