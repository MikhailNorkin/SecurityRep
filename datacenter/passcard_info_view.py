from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .get_time import format_time


def is_visit_long(visit_in_time , mins = 60 ):
    '''Функция проверяет на подозрительность сотрудника'''

    if visit_in_time > mins * 60:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    ''' Функция выводит Список всех посещений определенного посетителя и проводит проверку на подозрительность'''

    visitors_list = []
    passcard_visit = Passcard.objects.get(passcode = passcode)
    visits = Visit.objects.filter(passcard = passcard_visit)
    for visit_inside in visits:
        delta = visit_inside.leaved_at - visit_inside.entered_at
        seconds = delta.total_seconds() 
        time_when = format_time(seconds)
        time_inside = is_visit_long(seconds)
        visitors_dict = {
            "entered_at": visit_inside.entered_at,
            "duration": time_when,
            'is_strange': time_inside
            }
        visitors_list.append(visitors_dict)

    this_passcard_visits = visitors_list
    context = {
        'passcard': passcard_visit,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
