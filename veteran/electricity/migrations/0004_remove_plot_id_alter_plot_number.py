# Generated by Django 5.0.6 on 2024-06-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electricity', '0003_alter_person_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='id',
        ),
        migrations.AlterField(
            model_name='plot',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]