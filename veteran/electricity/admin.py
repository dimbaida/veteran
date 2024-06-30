from django.contrib import admin
from .models import Measurement, Plot


admin.site.register(Measurement)
admin.site.register(Plot)
