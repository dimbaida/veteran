from django.db import models
from django.conf import settings


class Measurement(models.Model):
    plot = models.IntegerField(default=0, verbose_name='Ділянка')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Показ надав', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата', null=True, blank=True)
    value_day = models.IntegerField(verbose_name='Денний тариф')
    value_night = models.IntegerField(verbose_name='Нічний тариф')

    def __str__(self):
        if self.user:
            name = f'{self.user.lastname} {self.user.firstname}' if self.user else ' --- '
        else:
            name = ' --- '
        return f"[{name}][{self.date.strftime('%d.%m.%Y')}] Ділянка {self.plot} | Д: {self.value_day}, Н: {self.value_night}"
