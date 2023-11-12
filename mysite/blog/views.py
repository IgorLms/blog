from django.shortcuts import render, get_object_or_404

from .models import Post
from .services.services import pagination_page


def post_list(request):
    """Получение всех опубликованных постов с пагинацией"""

    posts_queryset = Post.published.all()
    page_number = request.GET.get('page', 1)

    posts = pagination_page(
        queryset=posts_queryset,
        per_page=3,
        page_number=page_number
    )

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    """Получение одного поста"""

    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})
