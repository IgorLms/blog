from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .services.validators import validate_email


class SignUpForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    username = forms.CharField(max_length=100, label='Логин')
    email = forms.EmailField(validators=[validate_email], label='Почта')
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
