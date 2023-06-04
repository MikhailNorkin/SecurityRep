from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from math import floor

def get_duration(visit):
    '''Функция возвращает количество секунд от текущего момента до даты начала визита'''

    delta = timezone.localtime() - visit.entered_at
    seconds = delta.total_seconds()
    return seconds 

def format_duration(duration):
    '''Фунция переводит секунды в часы и минуты'''

    hours = floor(duration // 3600)
    mins = floor((duration-hours*3600) // 60)
    return print(str(hours)+'ч '+str(mins)+'мин')

def format_time(seconds):
    '''Функция переводит секунды в часы, минуты и секунды'''

    hours = floor(seconds // 3600)
    mins = floor((seconds-hours*3600) // 60)
    secs = floor(seconds - hours * 3600 - mins * 60)
    return '{}:{:02}:{:02}'.format(hours, mins, secs)

def storage_information_view(request):
    '''Функция получает активные визиты пользователей'''

    my_list = []
    visit_in = Visit.objects.filter(leaved_at = None)
    for visit in visit_in:
        seconds = get_duration(visit)  
        time_inside = format_time(seconds)
        passcard = visit.passcard
        pas_name = str(passcard.owner_name)
        time_in = visit.entered_at
        my_dict = {
            "who_entered": pas_name,
            "entered_at": time_in,
            'duration': time_inside
            }
        my_list.append(my_dict)

    non_closed_visits = my_list
    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
    


