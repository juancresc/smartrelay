from .models import Alarm
from django.utils import timezone
from datetime import datetime
class CalculateCurrentStatus():

    def execute(self):
        now = datetime.now().time()
        
        #prev alarm, any previous at now
        closest_alarm = Alarm.objects.filter(alarm_time__lte=now)
        closest_alarm = closest_alarm.order_by('-alarm_time')
        closest_alarm = closest_alarm.first()
        if closest_alarm:
            return closest_alarm.action

        #latest alarm, the one that is more late
        closest_alarm = Alarm.objects.all()
        closest_alarm = closest_alarm.order_by('-alarm_time')
        closest_alarm = closest_alarm.first()
        if closest_alarm:
            return closest_alarm.action

        #no alarm, keep it off
        return False