# Generated by Django 3.1.4 on 2021-08-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20210830_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='head',
            name='time',
            field=models.DecimalField(decimal_places=3, max_digits=25),
        ),
        migrations.AlterField(
            model_name='listen',
            name='time',
            field=models.DecimalField(decimal_places=3, max_digits=25),
        ),
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.DecimalField(decimal_places=3, max_digits=25),
        ),
    ]
