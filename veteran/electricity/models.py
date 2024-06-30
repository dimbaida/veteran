from django.db import models
from django.conf import settings


class Plot(models.Model):
    number = models.CharField(primary_key=True)
    balance = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Ділянка'
        verbose_name_plural = 'Ділянки'

    def __str__(self):
        return self.number


class Measurement(models.Model):
    plot = models.CharField(default='', verbose_name='Ділянка')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Показ надав', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата', null=True, blank=True)
    value_day = models.IntegerField(verbose_name='День')
    value_night = models.IntegerField(verbose_name='Ніч', blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Показ'
        verbose_name_plural = 'Покази'

    def __str__(self):
        name = f'{self.user.lastname} {self.user.firstname}' if self.user else ' --- '
        return f"[{name}][{self.date.strftime('%d.%m.%Y')}] Ділянка {self.plot} | Д: {self.value_day}, Н: {self.value_night}"