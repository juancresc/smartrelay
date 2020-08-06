from django.contrib import admin
from .models import Alarm, OnOff

# Register your models here.
admin.site.register(Alarm)
admin.site.register(OnOff)
