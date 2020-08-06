from .models import Alarm, OnOff
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class CalculateCurrentStatus():

    def execute(self):
        now = timezone.now().time()
        today = timezone.now().date()
        yesterday = today - timedelta(days=1)
        return_alarm = False
        #prev alarm, any previous at now
        closest_alarm = Alarm.objects.filter(alarm_time__lte=now)
        closest_alarm = closest_alarm.order_by('-alarm_time')
        closest_alarm = closest_alarm.first()
        if closest_alarm:
            #if it was not created today or it was created
            #before the alarm time, dismiss it
            if closest_alarm.updated_at.date() != today or closest_alarm.updated_at.time() < closest_alarm.alarm_time:
                return_alarm = closest_alarm
        else:
            #latest alarm, the one that is more late
            closest_alarm = Alarm.objects.all()
            closest_alarm = closest_alarm.order_by('-alarm_time')
            closest_alarm = closest_alarm.first()
            updated_at = closest_alarm.updated_at
            if closest_alarm:
                #only if it was created yesterday before the alarm time
                if updated_at.date() <= yesterday and updated_at.time() < closest_alarm.alarm_time:
                    return_alarm = closest_alarm
        if return_alarm:
            #if the alarm is a time in the past
            print(return_alarm)
            if return_alarm.alarm_time <= now:
                #if there's an OnOff event posterior to the alarm
                on_off = OnOff.objects.filter(updated_at__date=today)
                on_off = on_off.filter(updated_at__time__gte=return_alarm.alarm_time)
                on_off = on_off.first()
                if on_off:
                    return on_off.action
            else:
                #if the alarm is a time in the future
                on_off = OnOff.objects.filter(updated_at__date__gte=yesterday)
                on_off = on_off.filter(updated_at__time__gte=return_alarm.alarm_time)
                on_off = on_off.first()
                if on_off:
                    return on_off.action
            return return_alarm.action
        else:
            on_off = OnOff.objects.all().first()
            if on_off:
                return on_off.action

        #no alarm, keep it off
        return False