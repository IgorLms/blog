from typing import Optional

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet, Count
from django.shortcuts import get_object_or_404
from taggit.models import Tag

from ..forms import CommentForm
from ..models import Post


def pagination_page(queryset: QuerySet, per_page: int, page_number: int) -> QuerySet:
    """Пагинация страницы"""

    paginator = Paginator(queryset, per_page)
    try:
        paginator_queryset = paginator.page(page_number)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)
    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages)

    return paginator_queryset


def add_comment_to_post(form: CommentForm, post: Post) -> CommentForm:
    """Сохранение валидного комментария и привязка его к посту"""

    comment = form.save(commit=False)
    comment.post = post
    comment.save()

    return comment


def post_filter_tag(tag_slug: Optional[str], posts_queryset: QuerySet, tag=None) -> tuple[Optional[Tag], QuerySet]:
    """Фильтрация постов по тегу"""

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts_queryset = posts_queryset.filter(tags__in=[tag])

    return tag, posts_queryset


def list_of_similar_posts(post: Post, num_of_post: int) -> Post:
    """Получение схожих постов"""

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.pk)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:num_of_post]

    return similar_posts


def search_post(query: str) -> Post:
    """Поиск поста по заголовку и статье"""

    # Поиск по нескольким полям
    search_vector = SearchVector('title', 'body', config='russian')
    # Выделение основы слова и ранжирование результата
    search_query = SearchQuery(query, config='russian')

    results = Post.published.annotate(
        search=search_vector,
        rank=SearchRank(
            search_vector,
            search_query
        )
    ).filter(
        search=search_query
    ).order_by(
        '-rank'
    )

    return results
