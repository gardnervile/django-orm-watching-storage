from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datacenter.storage_information_view import format_duration, is_visit_strange


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        entered_at = timezone.localtime(visit.entered_at)
        leaved_at = timezone.localtime(visit.leaved_at)
        duration = leaved_at - entered_at
        is_strange = is_visit_strange(duration)

        this_passcard_visits.append({
            'entered_at': entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)