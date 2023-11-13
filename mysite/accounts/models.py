from django.db import models
from django.contrib.auth.models import User
from PIL import Image


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

    def save(self, *args, **kwargs):
        """Изменим размер аватара"""

        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
