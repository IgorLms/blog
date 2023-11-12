from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts() -> Post:
    """Подсчёт числа постов"""

    return Post.published.count()


@register.simple_tag
def get_most_commented_posts(count: int = 5) -> Post:
    """Вывод самых закомментированных постов"""

    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count: int = 5) -> dict[str: Post]:
    """Вывод последних постов пользователя"""

    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
