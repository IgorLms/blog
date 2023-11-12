from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """Получение всех опубликованных постов"""

    posts = Post.published.all()

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id_post):
    """Получение одного поста"""

    post = get_object_or_404(Post, id=id_post, status=Post.Status.PUBLISHED)

    return render(request, 'blog/post/detail.html', {'post': post})
