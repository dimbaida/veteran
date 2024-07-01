from django.db import models
from django.conf import settings


class Plot(models.Model):
    verbose = models.CharField(max_length=5, default='')
    balance = models.FloatField(default=0)
    value_night_avg = models.IntegerField(blank=True, null=True)
    value_day_avg = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Ділянка'
        verbose_name_plural = 'Ділянки'

    def __str__(self):
        return self.verbose


class Measurement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT,
                             related_name='measurements',
                             verbose_name='Показ надав',
                             null=True,
                             blank=True)
    plot = models.ForeignKey(Plot,
                             on_delete=models.PROTECT,
                             verbose_name='Ділянка',)
    value_day = models.IntegerField(verbose_name='День')
    value_night = models.IntegerField(verbose_name='Ніч',
                                      blank=True,
                                      null=True)
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name='Дата')
    is_paid = models.BooleanField(default=False,
                                  verbose_name='Оплачено')
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='approved_measurements',
                                    on_delete=models.PROTECT,
                                    null=True,
                                    blank=True)
    approved_date = models.DateTimeField(verbose_name='Дата',
                                         null=True,
                                         blank=True)
    comment = models.CharField(default='',
                               verbose_name='comment',
                               null=True,
                               blank=True)

    class Meta:
        verbose_name = 'Показ'
        verbose_name_plural = 'Покази'

    def __str__(self):
        return f"[{self.date.strftime('%d.%m.%Y')}] Ділянка {self.plot} | Д: {self.value_day}, Н: {self.value_night}"


class Resident(models.Model):
    plot = models.ForeignKey(Plot,
                             on_delete=models.PROTECT,
                             verbose_name='Ділянка')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT,
                             verbose_name='Показ надав')

    class Meta:
        verbose_name = 'Резидент'
        verbose_name_plural = 'Резиденти'

    def __str__(self):
        return f"{self.plot.verbose_name} :: {self.user.lastnme} {self.user.firstname}"
