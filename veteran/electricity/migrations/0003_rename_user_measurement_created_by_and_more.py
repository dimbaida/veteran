# Generated by Django 5.0.6 on 2024-07-02 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0002_remove_measurement_is_approved_measurement_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='measurement',
            old_name='approved_date',
            new_name='date_approved',
        ),
        migrations.RenameField(
            model_name='measurement',
            old_name='date',
            new_name='date_created',
        ),
    ]
