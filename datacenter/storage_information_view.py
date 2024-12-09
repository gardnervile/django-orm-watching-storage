from django.utils.timezone import localtime
from datacenter.models import Visit
from django.shortcuts import render


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
STRANGE_VISIT_THRESHOLD_SECONDS = SECONDS_IN_HOUR  # 1 час


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    seconds = total_seconds % SECONDS_IN_MINUTE
    return f'{hours:02}:{minutes:02}:{seconds:02}'


def is_visit_strange(duration, threshold=STRANGE_VISIT_THRESHOLD_SECONDS):
    return duration.total_seconds() > threshold


def get_duration(entered_at):
    entered_at_local = localtime(entered_at)
    time_in_storage = localtime() - entered_at_local
    return time_in_storage


def storage_information_view(request):
    non_closed_visits = []
    ongoing_visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in ongoing_visits:
        passcard_owner = visit.passcard.owner_name
        entered_at_local = localtime(visit.entered_at)
        duration = get_duration(visit.entered_at)

        non_closed_visits.append({
            'who_entered': passcard_owner,
            'entered_at': entered_at_local.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)