# Generated by Django 3.1.4 on 2021-08-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20210830_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default='home', max_length=100),
        ),
    ]
