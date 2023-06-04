from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import format_time
from django.shortcuts import get_object_or_404


def is_visit_long(visit_in_time , mins = 60 ):
    '''Функция проверяет на подозрительность сотрудника'''
    if visit_in_time > mins * 60:
        return True
    else:
        return False

def passcard_info_view(request, passcode):
    ''' Функция выводит Список всех посещений определенного посетителя и проводит проверку на подозрительность'''

    get_object_or_404(Passcard, passcode = passcode)
    my_list = []
    passcard_visit = Passcard.objects.get(passcode = passcode)
    visits = Visit.objects.filter(passcard = passcard_visit)
    for visit_in in visits:
        delta = visit_in.leaved_at - visit_in.entered_at
        seconds = delta.total_seconds() 
        time_in = format_time(seconds)
        time_inside = is_visit_long(seconds)
        my_dict = {
            "entered_at": visit_in.entered_at,
            "duration": time_in,
            'is_strange': time_inside
            }
        my_list.append(my_dict)

    this_passcard_visits = my_list
    context = {
        'passcard': passcard_visit,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
