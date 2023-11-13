from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Profile


@admin.register(Profile)
class MyProfile(SummernoteModelAdmin):
    """Модернизируем админ-панель для таблицы Profile"""

    summernote_fields = ('bio',)
