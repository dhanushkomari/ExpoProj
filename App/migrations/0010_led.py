# Generated by Django 3.1.4 on 2021-08-31 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20210830_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Led',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('time', models.DecimalField(decimal_places=3, max_digits=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'LED Setting',
                'verbose_name_plural': 'LED Settings',
                'ordering': ('-id',),
            },
        ),
    ]