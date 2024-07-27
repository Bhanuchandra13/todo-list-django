from django.urls import path
from users_app import views

from django.contrib.auth import views as auth_views

from .views import CustomLogoutView

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
]
