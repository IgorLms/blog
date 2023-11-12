from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import CommentForm
from .models import Post
from .services.services import pagination_page, add_comment_to_post, post_filter_tag


def post_list(request, tag_slug=None):
    """Получение всех опубликованных постов с пагинацией"""

    posts_queryset = Post.published.all()

    tag, posts_queryset = post_filter_tag(tag_slug, posts_queryset)

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

    comments = post.comments.filter(active=True)

    context = {'post': post,
               'comments': comments,
               'form': CommentForm()}
    return render(request, 'blog/post/detail.html', context)


@require_POST
def post_comment(request, post_id, comment=None):
    """Добавление комментария к посту"""

    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)

    form = CommentForm(data=request.POST)

    if form.is_valid():
        comment = add_comment_to_post(form, post)

    context = {
        'post': post,
        'form': form,
        'comment': comment
    }

    return render(request, 'blog/post/comment.html', context)
