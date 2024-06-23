
from django.contrib import admin

from .models import Plot, Person, Measurement

admin.site.register(Plot)
admin.site.register(Person)
admin.site.register(Measurement)