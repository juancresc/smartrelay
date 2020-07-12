from django.contrib import admin
from django.urls import path
from django.urls import include, path

app_name = "smartrelay"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alarms/', include('alarms.urls', namespace="alarms")),
]

admin.site.site_header = "Smart Relay"
admin.site.site_title = "Smart Relay Portal"
admin.site.index_title = "Smart Relay Administration"
