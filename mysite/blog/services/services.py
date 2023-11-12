from typing import Optional

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet
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
