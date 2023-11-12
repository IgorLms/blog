from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedPost(models.Manager):
    """Модельный менеджер для извлечения постов со статусом опубликовано"""
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Модель поста блога"""

    class Status(models.TextChoices):
        DRAFT = 'Черновик'
        PUBLISHED = 'Опубликована'

    title = models.CharField(max_length=250, verbose_name='Заголовок поста')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Slug поста')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор поста')
    body = models.TextField(verbose_name='Пост')

    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации поста')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения поста')
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PUBLISHED, verbose_name='Статус поста')

    objects = models.Manager()
    published = PublishedPost()

    class Meta:
        """Упорядочим посты по убыванию даты публикации поста и настроим индексацию по этому полю"""
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Генерация канонического URL-адреса для детальной информации о посте"""

        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )


class Comment(models.Model):
    """Модель комментария для поста"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')

    name = models.CharField(max_length=80, verbose_name='Имя комментатора')
    email = models.EmailField(verbose_name='Почта комментатора')
    body = models.TextField(verbose_name='Комментарий')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения комментария')

    active = models.BooleanField(default=True, verbose_name='Статус комментария')

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий {self.name} под постом {self.post}'
