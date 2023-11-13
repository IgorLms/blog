from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
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


class UpdateUserForm(forms.ModelForm):
    """Форма позволяет пользователям обновлять свое имя пользователя и адрес электронной почты"""
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(), label='Логин')
    email = forms.EmailField(required=True, widget=forms.TextInput(), label='Почта')

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    """Форма позволяет пользователям обновлять свой профиль"""

    avatar = forms.ImageField(widget=forms.FileInput(), label='Аватар')
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), label='Информация о пользователе')

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']