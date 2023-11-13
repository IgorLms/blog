from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма для ввода комментария"""

    name = forms.CharField(
        required=True,
        label='Имя',
        widget=forms.TextInput(
            attrs={"class": "form-control", 'placeholder': 'Name'}
        )
    )
    email = forms.EmailField(
        required=True,
        label='Почта',
        widget=forms.EmailInput(
            attrs={"class": "form-control", 'placeholder': 'Email'}
        )
    )
    body = forms.CharField(
        required=True,
        label='Комментарий',
        widget=SummernoteWidget(
            attrs={"class": "form-control", 'summernote': {'width': '100%', 'height': '300px'}}
        )
    )

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    """Форма для поиска"""

    query = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", 'placeholder': 'Введите запрос'}
        )
    )
