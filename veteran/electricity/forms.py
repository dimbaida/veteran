from django import forms
from .models import Measurement


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        exclude = ['user', 'plot', 'is_approved']
