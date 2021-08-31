from App.models import Service
from . import views
from django.urls import path

app_name = 'App'

urlpatterns = [
    path('', views.HomeView, name = 'home'),
    path('create-head', views.CreateHead, name = 'head-create'),
    path('create-listen', views.CreateListen, name = 'listen-create'),
    path('select-service/<int:id>', views.SelectService, name = 'select-service'),
    path('details/', views.AllDetails, name = 'all-details'),

    path('api/service', views.service_details, name = 'service-details'),
    path('api/head', views.head_details, name = 'head-details'),
    path('api/listen', views.listen_details, name = 'listen-details')
]

