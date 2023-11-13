from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, LoginView

from . import views
from .forms import LoginForm, ChangePassword

urlpatterns = [
    path(
            'login/',
            LoginView.as_view(
                template_name="registration/login.html",
                authentication_form=LoginForm
                ),
            name='login'
    ),
    path("signup/", views.signup, name="signup"),
    path('profile/', views.profile, name='users-profile'),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            form_class=ChangePassword
        ),
        name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
