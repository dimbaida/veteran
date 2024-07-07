from django import forms
from .models import Measurement, Resident, Plot


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('value_day', 'value_night', 'plot', 'comment')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            plots = Plot.objects.filter(resident__user=user)
            if plots.exists():
                self.fields['plot'].queryset = plots
                self.fields['plot'].initial = plots.first()  # Set initial value to the first plot
                self.fields['plot'].empty_label = None
            else:
                self.fields['plot'].queryset = Plot.objects.none()  # No plots available if none found
