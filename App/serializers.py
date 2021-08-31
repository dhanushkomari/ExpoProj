from rest_framework import serializers
from .models import Head, Listen, Service, SetService, Led

class HeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head
        fields = ('up_time', 'down_time', 'time')

class ListenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listen
        fields = ('listening_time', 'time')

class SetServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetService
        fields = ('service_name', 'time')

class LedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Led
        fields = ('status', 'time')
