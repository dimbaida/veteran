from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('measurements/', views.measurement_list, name='measurement_list'),
    path('measurements/add/', views.measurement_add, name='measurement_add')
]