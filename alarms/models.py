from django.db import models
from django.utils.timezone import now, timedelta


class Alarm(models.Model):
    alarm_time = models.TimeField()
    action = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        action = "ON" if self.action else "OFF"
        return "{} at {} ".format(action, self.alarm_time)


class OnOff(models.Model):
    action = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        action = "ON" if self.action else "OFF"
        return "{} at {} ".format(action, self.alarm_time)
