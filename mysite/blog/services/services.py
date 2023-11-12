from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet


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
