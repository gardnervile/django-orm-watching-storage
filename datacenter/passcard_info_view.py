from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datacenter.storage_information_view import format_duration, is_visit_strange


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = [
        {
            'entered_at': localtime(visit.entered_at).strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(visit.leaved_at - visit.entered_at),
            'is_strange': is_visit_strange(visit.leaved_at - visit.entered_at),
        }
        for visit in visits
    ]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
