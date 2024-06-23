from django.shortcuts import render
from .models import Measurement


def index(request):
    return render(request, 'index.html')


def history(request):
    measurements = Measurement.objects.all()
    verbose_names = {
        'date': Measurement._meta.get_field('date').verbose_name,
        'value_day': Measurement._meta.get_field('value_day').verbose_name,
        'value_night': Measurement._meta.get_field('value_night').verbose_name,
        'person': Measurement._meta.get_field('person').verbose_name,
        'plot': Measurement._meta.get_field('plot').verbose_name,
    }

    context = {'measurements': measurements,
               'verbose_names': verbose_names}

    return render(request, 'history.html', context)
