from django.db import models
from django.utils.timezone import now, timedelta


class Alarm(models.Model):
    alarm_time = models.TimeField()
    action = models.BooleanField()
    
    def __str__(self):
        action = "ON" if self.action else "OFF"
        return "{} at {} ".format(action, self.alarm_time)
