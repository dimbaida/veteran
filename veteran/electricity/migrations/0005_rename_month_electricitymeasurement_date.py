# Generated by Django 5.0.6 on 2024-06-23 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0004_remove_plot_id_alter_plot_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electricitymeasurement',
            old_name='month',
            new_name='date',
        ),
    ]