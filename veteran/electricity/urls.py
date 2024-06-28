from django.urls import path
from . import views

app_name = 'electricity'

urlpatterns = [
    path("", views.index, name="index"),
    path('measurements/', views.measurements, name='measurements'),
    path('measurements/add/', views.measurements_add, name='measurements_add')
]
