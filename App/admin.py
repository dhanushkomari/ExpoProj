from django.contrib import admin
from .models import Listen, Head, Service, SetService, Led

# Register your models here.

admin.site.register(Head)
admin.site.register(Service)
admin.site.register(Listen)
admin.site.register(SetService)
admin.site.register(Led)


