from django.contrib import admin

from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Модернизируем админ-панель для таблицы Post"""

    # Редактор WYSIWYG
    summernote_fields = ('body',)
    # Горизонтальное отображение полей поста
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # Панель фильтрации
    list_filter = ['status', 'created', 'publish', 'author']
    # Поле поиска
    search_fields = ['title', 'body']
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('title',)}
    # Поиск автора
    raw_id_fields = ['author']
    # Навигация по дате
    date_hierarchy = 'publish'
    # Сортировка
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """Модернизируем админ-панель для таблицы Comment"""

    summernote_fields = ('body',)
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
