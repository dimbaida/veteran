# Generated by Django 5.0.6 on 2024-07-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0005_alter_measurement_approved_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='value_night',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Ніч'),
        ),
    ]
