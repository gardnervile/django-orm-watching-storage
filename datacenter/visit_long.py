import os
import django
import sys
from datetime import timedelta
from django.utils.timezone import localtime


sys.path.append('/Users/evgenijkondratev/Desktop/django-orm-watching-storage')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from datacenter.models import Visit, Passcard


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime()
    return leaved_at - entered_at


def is_visit_long(visit, threshold_minutes=60):
    duration = get_duration(visit)
    threshold = timedelta(minutes=threshold_minutes)
    return duration > threshold


passcard_owner_name = 'Barbara Beck'
threshold_minutes = 10

try:
    passcard = Passcard.objects.get(owner_name=passcard_owner_name)
    print(f"Пропуск найден: {passcard.owner_name}")

    visits = Visit.objects.filter(passcard=passcard)
    long_visits = [visit for visit in visits if is_visit_long(visit, threshold_minutes)]

    if long_visits:
        print(f"Визиты дольше {threshold_minutes} минут:")
        for visit in long_visits:
            entered_at_local = localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M:%S')
            leaved_at_local = (
                localtime(visit.leaved_at).strftime('%d-%m-%Y %H:%M:%S') if visit.leaved_at else 'Не покинул'
            )
            duration = get_duration(visit)
            print(f"Вход: {entered_at_local} | Выход: {leaved_at_local} | Длительность: {duration}")
    else:
        print(f"Визитов дольше {threshold_minutes} минут не найдено.")

except Passcard.DoesNotExist:
    print(f"Пропуск с владельцем {passcard_owner_name} не найден.")
