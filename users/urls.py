"""Defines URL patterns for users module"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # Login page
    path(r'login/',
        LoginView.as_view(template_name='users/login.html'),name='login'),

    # Logout page
    path(r'logout/',
        LogoutView.as_view(template_name='learning_logs/index.html'),
        name='logout'),

    # Registration page
    path(r'register/', views.register, name='register'),
]
