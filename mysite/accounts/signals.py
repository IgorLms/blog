from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Сигнал приёмник. При создании нового пользователя создадим новый профиль."""

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Отправитель сигнала. Отправить сигнал в create_profile, чтобы создать профиль."""

    instance.profile.save()
