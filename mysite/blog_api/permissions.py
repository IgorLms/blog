from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Настройка прав доступа"""

    def has_permission(self, request, view):
        """Только аутентифицированные пользователи могут видеть представление списка"""

        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """Права на запись разрешены только автору сообщения"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
