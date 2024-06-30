from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Measurement, Resident
from .forms import MeasurementForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required
def measurements_add(request):

    # if not request.user.is_authenticated:
    #     return redirect(reverse('authuser:login'))

    if request.method == 'POST':
        form = MeasurementForm(request.POST, user=request.user)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user
            measurement.save()
            return redirect(reverse('electricity:measurements'))
    else:
        form = MeasurementForm(user=request.user)
    return render(request, 'measurements_add.html', {'form': form})


def measurements(request):
    user = request.user
    plots = user.resident_set.values_list('plot__id', flat=True)  # Get IDs of plots associated with the user

    if not user.is_authenticated:
        return redirect(reverse('authuser:login'))

    verbose_names = {
        'date': Measurement._meta.get_field('date').verbose_name,
        'value_day': Measurement._meta.get_field('value_day').verbose_name,
        'value_night': Measurement._meta.get_field('value_night').verbose_name,
        'user': Measurement._meta.get_field('user').verbose_name,
        'plot': Measurement._meta.get_field('plot').verbose_name,
    }

    context = {'measurements': Measurement.objects.filter(plot__id__in=plots).order_by('date'),
               'verbose_names': verbose_names}

    return render(request, 'measurements.html', context)
