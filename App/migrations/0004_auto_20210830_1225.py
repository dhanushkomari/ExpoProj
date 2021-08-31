# Generated by Django 3.1.4 on 2021-08-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_service_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='head',
            name='time',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='listen',
            name='time',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]