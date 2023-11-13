from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Серилизатора для постов"""

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created",
        )
        model = Post
