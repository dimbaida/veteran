# Generated by Django 5.0.6 on 2024-07-02 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0003_rename_user_measurement_created_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='is_paid',
            new_name='paid',
        ),
    ]