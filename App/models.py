from django.db import models
from django.urls import reverse

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length = 25)
    created_at = models.DateTimeField(auto_now_add = True)
    time = models.DecimalField(max_digits = 25,decimal_places=3)
    icon = models.CharField(max_length=100, default = 'home')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        # return reverse()
        pass

class Listen(models.Model):
    listening_time = models.IntegerField(help_text='in seconds', default=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time = models.DecimalField(max_digits = 25,decimal_places=3)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Listening Time'
        verbose_name_plural = 'Listening Time'

    def __str__(self):
        return str(self.listening_time)


class Head(models.Model):
    up_time = models.IntegerField(help_text='In seconds', default=10)
    down_time = models.IntegerField(help_text='In seconds', default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)
    time = models.DecimalField(max_digits = 25,decimal_places=3)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Head Setting'
        verbose_name = 'Head Settings'

    def __str__(self):
        return "{}".format("Head Settting "+str(self.id))

class SetService(models.Model):
    service_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)
    time = models.DecimalField(max_digits=30, decimal_places=3)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'SetService'
        verbose_name_plural = 'Set Services'

    def __str__(self):
        return self.service_name


class Led(models.Model):
    status  = models.BooleanField(default=True)
    time = models.DecimalField(max_digits=30, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'LED Setting'
        verbose_name_plural = 'LED Settings'

    def __str__(self):
        return str(self.status)