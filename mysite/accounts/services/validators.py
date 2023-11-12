from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_email(value: str):
    """Проверка на уникальность почты"""

    if User.objects.filter(email=value).exists():
        raise ValidationError(
            f"{value} существует",
            params={'value': value}
        )
