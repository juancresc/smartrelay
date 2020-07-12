from .models import Alarm
from django.utils import timezone
from datetime import datetime
class CalculateCurrentStatus():

    def execute(self):
        now = datetime.now().time()
        print(now)
        closest_alarm = Alarm.objects.filter(alarm_time__lte=now)
        closest_alarm = closest_alarm.order_by('-alarm_time')
        closest_alarm = closest_alarm.first()
        print(closest_alarm)
        if closest_alarm:
            return closest_alarm.action
        return False