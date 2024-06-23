# Generated by Django 5.0.6 on 2024-06-23 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0002_person_email_person_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Mobile number must be in the format of "380XXXXXXXXX".', regex='^380\\d{9}$')]),
        ),
    ]
