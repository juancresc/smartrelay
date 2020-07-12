from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

app_name = "alarms"

urlpatterns = [
    path('', views.ConnectView.as_view(), name='connect'),
]
