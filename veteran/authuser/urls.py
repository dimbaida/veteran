from django.urls import path
from .views import register, custom_login

app_name = 'authuser'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login, name='login')
]
