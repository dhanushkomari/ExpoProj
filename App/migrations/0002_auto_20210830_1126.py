# Generated by Django 3.1.4 on 2021-08-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='head',
            name='time',
            field=models.DecimalField(decimal_places=6, default=12333, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listen',
            name='time',
            field=models.DecimalField(decimal_places=6, default=33333, max_digits=15),
            preserve_default=False,
        ),
    ]
