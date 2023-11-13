from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django_summernote.widgets import SummernoteWidget

from .models import Profile
from .services.validators import validate_email


class SignUpForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    first_name = forms.CharField(
        max_length=100,
        label='Имя',
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1"}
        )
    )
    last_name = forms.CharField(
        max_length=100,
        label='Фамилия',
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1"}
        )
    )
    username = forms.CharField(
        max_length=100,
        label='Логин',
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1"}
        )
    )
    email = forms.EmailField(
        validators=[validate_email],
        label='Почта',
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1"}
        )
    )
    password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1"}
        ),
        label='Пароль'
    )
    password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1"}
        ),
        label='Повторите пароль'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    """Форма позволяет пользователям обновлять свое имя пользователя и адрес электронной почты"""
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1"}
        ),
        label='Логин'
     )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1"}
        ),
        label='Почта'
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    """Форма позволяет пользователям обновлять свой профиль"""

    avatar = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class": "form-control mb-1"}
        ),
        label='Аватар'
    )
    bio = forms.CharField(
        widget=SummernoteWidget(
            attrs={"class": "form-control", 'summernote': {'width': '100%', 'height': '300px'}}
        ),
        label='Информация о пользователе'
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class LoginForm(AuthenticationForm):
    """Форма для авторизации"""

    username = forms.CharField(
        max_length=100,
        label='Логин',
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1"}
        )
    )
    password = forms.CharField(
        max_length=50,
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1"}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class ChangePassword(PasswordChangeForm):
    """Форма для изменения пароля"""

    old_password = forms.CharField(
        max_length=50,
        label='Старый пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1"}
        )
    )
    new_password1 = forms.CharField(
        max_length=50,
        label='Новый пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1"}
        )
    )
    new_password2 = forms.CharField(
        max_length=50,
        label='Повторение нового пароля',
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-1"}
        )
    )

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]

