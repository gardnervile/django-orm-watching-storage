import os
import django
import sys
from datetime import timedelta
from django.utils.timezone import localtime


sys.path.append('/Users/evgenijkondratev/Desktop/django-orm-watching-storage')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from datacenter.models import Visit


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime()
    return leaved_at - entered_at


def is_visit_long(visit, threshold_minutes=60):
    duration = get_duration(visit)
    threshold = timedelta(minutes=threshold_minutes)
    return duration > threshold
