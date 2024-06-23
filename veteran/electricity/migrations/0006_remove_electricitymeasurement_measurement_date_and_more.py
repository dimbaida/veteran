# Generated by Django 5.0.6 on 2024-06-23 19:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0005_rename_month_electricitymeasurement_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electricitymeasurement',
            name='measurement_date',
        ),
        migrations.AlterField(
            model_name='electricitymeasurement',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='electricitymeasurement',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='electricity.person', verbose_name='Показ надав'),
        ),
        migrations.AlterField(
            model_name='electricitymeasurement',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='electricity.plot', verbose_name='Ділянка'),
        ),
        migrations.AlterField(
            model_name='electricitymeasurement',
            name='value_day',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Денний тариф'),
        ),
        migrations.AlterField(
            model_name='electricitymeasurement',
            name='value_night',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Нічний тариф'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Призвище'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Mobile number must be in the format of "380XXXXXXXXX".', regex='^380\\d{9}$')], verbose_name='Номер телефону'),
        ),
        migrations.AlterField(
            model_name='person',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='electricity.plot', verbose_name='Ділянка'),
        ),
    ]