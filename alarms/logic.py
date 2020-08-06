from .models import Alarm, OnOff
from django.utils import timezone
from datetime import datetime
class CalculateCurrentStatus():

    def execute(self):
        now = datetime.now().time()
        today = timezone.now().date()
        yesterday = today - datetime.timedelta(days=1)
        return_alarm = False
        #prev alarm, any previous at now
        closest_alarm = Alarm.objects.filter(alarm_time__lte=now)
        closest_alarm = closest_alarm.order_by('-alarm_time')
        closest_alarm = closest_alarm.first()
        created_at = closest_alarm.created_date
        if closest_alarm:
            #if it was not created today or it was created
            #before the alarm time, dismiss it
            if created_at.date() != today or created_at.time() < closest_alarm.alarm_time:
                return_alarm = closest_alarm.action

        #latest alarm, the one that is more late
        closest_alarm = Alarm.objects.all()
        closest_alarm = closest_alarm.order_by('-alarm_time')
        closest_alarm = closest_alarm.first()
        created_at = closest_alarm.created_date
        if closest_alarm:
            #only if it was created yesterday before the alarm time
            if created_at.date() <= yesterday and created_at.time() < closest_alarm.alarm_time:
                return_alarm = closest_alarm.action
                
        if return_alarm:
            #if the alarm is a time in the past
            if return_alarm.alarm_time <= now:
                #if there's an OnOff event posterior to the alarm
                on_off = OnOff.objects.filter(created_at=today)
                on_off = on_off.filter(created_at__time__gte=return_alarm.alarm_time)
                on_off = on_off.first()
                if on_off:
                    return on_off.action
            else:
                #if the alarm is a time in the future
                on_off = OnOff.objects.filter(created_at__gte=yesterday)
                on_off = on_off.filter(created_at__time__gte=return_alarm.alarm_time)
                on_off = on_off.first()
                if on_off:
                    return on_off.action
            return return_alarm.action

        #no alarm, keep it off
        return False