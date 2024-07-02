from django.urls import path
from .views import register, custom_login
from django.contrib.auth import views as auth_views

app_name = 'authuser'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done')
]
