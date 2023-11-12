from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма для ввода комментария"""
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
