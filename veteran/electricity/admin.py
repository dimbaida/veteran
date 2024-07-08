from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Measurement, Plot, Resident
from django import forms


class MeasurementAdminForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved_by'].queryset = get_user_model().objects.filter(is_staff=True)
        # Preselect current user for approved_by if creating new measurement
        if not self.instance.approved_by:
            self.initial['approved_by'] = self.fields['approved_by'].initial = self.instance.created_by


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    form = MeasurementAdminForm

    # Customize other admin options as needed
    list_display = ('plot', 'created_by', 'value_day', 'value_night', 'date_created', 'paid', 'approved_by', 'date_approved')
    list_filter = ('date_created', 'date_approved', 'paid')


admin.site.register(Plot)
admin.site.register(Resident)
