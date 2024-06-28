from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Measurement
from .forms import MeasurementForm
import datetime


def index(request):
    return render(request, 'index.html')


def measurements_add(request):
    user = request.user

    if not user.is_authenticated:
        return redirect(reverse('authuser:login'))

    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = user
            measurement.plot = user.plot
            # measurement.month = datetime.datetime.now().month
            # measurement.year = datetime.datetime.now().year
            measurement.save()
            return redirect(reverse('electricity:measurements'))
    else:
        form = MeasurementForm()
    return render(request, 'measurements_add.html', {'form': form})


def measurements(request):
    user = request.user

    if not user.is_authenticated:
        return redirect(reverse('authuser:login'))

    measurements = Measurement.objects.filter(plot=user.plot)

    verbose_names = {
        'date': Measurement._meta.get_field('date').verbose_name,
        'value_day': Measurement._meta.get_field('value_day').verbose_name,
        'value_night': Measurement._meta.get_field('value_night').verbose_name,
        'user': Measurement._meta.get_field('user').verbose_name,
        'plot': Measurement._meta.get_field('plot').verbose_name,
    }

    context = {'measurements': measurements,
               'verbose_names': verbose_names}

    return render(request, 'measurements.html', context)
