from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path('profile/', views.profile, name='users-profile'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
