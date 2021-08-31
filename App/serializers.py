from rest_framework import serializers
from .models import Head, Listen, Service

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = ('up_time', 'down_time', 'time')

class ListenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listen
        fields = ('listening_time', 'time')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'time')