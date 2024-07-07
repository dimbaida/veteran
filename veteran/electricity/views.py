from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Measurement, Resident, Plot
from .forms import MeasurementForm
from .services.paycheck import Paycheck


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
            measurement.created_by = request.user
            measurement.save()
            return redirect(reverse('electricity:measurements'))
    else:
        form = MeasurementForm(user=request.user)
    return render(request, 'measurements_add.html', {'form': form})


def measurements(request):

    user = request.user

    if not user.is_authenticated:
        return redirect(reverse('authuser:login'))

    plots = user.resident_set.values_list('plot__id', flat=True)  # Get IDs of plots associated with the user
    measurements = Measurement.objects.filter(plot__id__in=plots).order_by('-date_created')
    verbose_names = {
        'date_created': Measurement._meta.get_field('date_created').verbose_name,
        'value_day': Measurement._meta.get_field('value_day').verbose_name,
        'value_night': Measurement._meta.get_field('value_night').verbose_name,
        'created_by': Measurement._meta.get_field('created_by').verbose_name,
        'plot': Measurement._meta.get_field('plot').verbose_name,
        'paid': Measurement._meta.get_field('paid').verbose_name
    }

    context = {'measurements': measurements,
               'verbose_names': verbose_names}

    return render(request, 'measurements.html', context)


@login_required
def compose_paycheck(request, plot_id, value_day_curr, value_night_curr):
    user = request.user
    plot = Plot.objects.get(id=plot_id)
    value_day_prev = 0
    value_night_prev = 0

    # print(f'user: {user}\nplot: {plot}\nvalue_day_curr: {value_day_curr}\nvalue_night_curr: {value_night_curr}')

    if request.method == 'POST':
        paycheck = Paycheck(consumer=user.lastname,
                            agreement=f"№{plot.verbose} від 01.06.2024",
                            month='вересень',
                            value_day_prev=value_day_prev,
                            value_day_curr=value_day_curr,
                            value_night_prev=value_night_prev,
                            value_night_curr=value_night_curr,
                            purpose=f'Договір №{plot.verbose} від 01.06.2024 р., {user.lastname}.\n'
                                    f'День: {value_day_curr}, Ніч: {value_night_curr}, в т.ч. технологічні витрати')

        pdf_buffer = paycheck.render()

        # Create a response with the PDF file
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="paycheck.pdf"'

        return response
