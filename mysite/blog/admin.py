from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Модернизируем админ-панель для таблицы Post"""

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
