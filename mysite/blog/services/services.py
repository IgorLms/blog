from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet

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
