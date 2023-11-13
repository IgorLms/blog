from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters

from .pagination import StandardResultsSetPagination
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    """Получение всех постов"""

    # Права доступа
    permission_classes = (IsAuthorOrReadOnly,)
    # queryset для запроса
    queryset = Post.objects.all()
    # Класс серилизатора
    serializer_class = PostSerializer
    # Кто отвечает за фильтрацию
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Фильтрация по автору
    filterset_fields = ['author']
    # Фильтрация элементов по посту
    search_fields = ['body']
    # Упорядочивание результата по id автора и дате публикации
    ordering_fields = ['author_id', 'publish']
    # Упорядочивание по умолчанию
    ordering = ['body']
    #  Пагинация
    pagination_class = StandardResultsSetPagination


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Получение одного поста"""

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
