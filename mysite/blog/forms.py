from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма для ввода комментария"""

    body = forms.CharField(required=True, widget=SummernoteWidget(), label='Комментарий')

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    """Форма для поиска"""

    query = forms.CharField()
