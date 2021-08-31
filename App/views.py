from typing import List, Set

from django.http import request
from App.serializers import HeadSerializer, ListenSerializer, SetServiceSerializer, LedSerializer
from django.shortcuts import render, redirect
from.models import Led, Service, Listen, Head, SetService, Led

from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
from django.contrib import messages

# Create your views here.

def HomeView(request):
    qs  =  Service.objects.all()
    return render(request, 'App/index.html', {'qs':qs})

def AllDetails(request):
    service = SetService.objects.latest('pk')
    head = Head.objects.latest('pk')
    listen = Listen.objects.latest('pk')
    return render(request, 'App/detail.html', {'service':service, 'head':head, 'listen':listen})




def CreateHead(request):
    if request.method == "POST":
        
        up_time = request.POST['up_time']
        down_time = request.POST['down_time']
        obj = Head.objects.latest('pk')
        obj.up_time = up_time
        obj.down_time = down_time
        obj.time = time.time()
        obj.save()
        messages.info(request, 'Head settings updated succesfully')


        return redirect('App:home')
    return render(request, 'App/head.html')



def CreateListen(request):
    if request.method == "POST":
        
        listen_time = request.POST['listen_time']
        obj = Listen.objects.latest('pk')
        obj.listening_time = listen_time
        obj.time = time.time()
        obj.save()
        messages.info(request, 'Listening settings updated succesfully')

        return redirect('App:home')
    return render(request, 'App/listen.html')

def SelectService(request, id):
    obj = Service.objects.get(id = id)
    print(obj.name)

    set = SetService.objects.latest('pk')

    set.service_name = obj.name
    set.time = time.time()
    set.save()
    messages.info(request, set.service_name+' Conversation Service started succesfully')
    return redirect('App:home')







#######################    REST VIEWS     #######################
@api_view(['GET'])
def head_details(request):
    data = Head.objects.latest('pk')
    serializer = HeadSerializer(data, many = False)
    return Response(serializer.data)

    
@api_view(['GET'])
def listen_details(request):
    data = Listen.objects.latest('pk')
    serializer = ListenSerializer(data, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def service_details(request):
    data = SetService.objects.latest('pk')
    serializer = SetServiceSerializer(data, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def led_details(request):
    data = Led.objects.latest('pk')
    serializer = LedSerializer(data, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def led_post(request):
    l = Led.objects.latest('pk')
    serializer = LedSerializer(instance = l, data = request.POST)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
