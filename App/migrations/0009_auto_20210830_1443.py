# Generated by Django 3.1.4 on 2021-08-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_setservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='head',
            name='down_time',
            field=models.IntegerField(default=10, help_text='In seconds'),
        ),
        migrations.AlterField(
            model_name='head',
            name='up_time',
            field=models.IntegerField(default=10, help_text='In seconds'),
        ),
        migrations.AlterField(
            model_name='listen',
            name='listening_time',
            field=models.IntegerField(default=7, help_text='in seconds'),
        ),
    ]
