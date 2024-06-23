from django.db import models
from django.core.validators import RegexValidator, EmailValidator


class Plot(models.Model):
    number = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.number}"


class Person(models.Model):
    username = models.CharField(max_length=50, verbose_name="Юзернейм")
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name='Призвище')
    mobile = models.CharField(
        max_length=12,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(regex=r'^380\d{9}$', message='Mobile number must be in the format of "380XXXXXXXXX".')],
        verbose_name='Номер телефону'
    )
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True, validators=[EmailValidator()])
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='residents', verbose_name='Ділянка')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Measurement(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name='measurements', verbose_name='Ділянка')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='measurements', verbose_name='Показ надав')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Денний тариф')
    value_night = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Нічний тариф')

    def __str__(self):
        return (f"[{self.date.strftime('%d.%m.%Y')}] Ділянка {self.plot.number}. Покази надав {self.person}. Д: {self.value_day}, Н: {self.value_night}")

