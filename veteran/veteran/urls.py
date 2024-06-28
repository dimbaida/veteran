from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authuser/', include('authuser.urls')),
    path('electricity/', include('electricity.urls')),
    path('', lambda request: redirect('electricity/measurements/', permanent=True)),
]

