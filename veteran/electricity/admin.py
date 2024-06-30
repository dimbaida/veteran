from django.contrib import admin
from .models import Measurement, Plot, Resident

admin.site.register(Measurement)
admin.site.register(Plot)
admin.site.register(Resident)
