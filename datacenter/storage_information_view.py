from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .get_time import get_duration, format_time


def storage_information_view(request):
    '''Функция получает активные визиты пользователей'''

    visitors_list = []
    visit_inside = Visit.objects.filter(leaved_at = None)
    for visit_active in visit_inside:
        seconds = get_duration(visit_active)  
        time_inside = format_time(seconds)
        passcard = visit_active.passcard
        pas_name = str(passcard.owner_name)
        time_when = visit_active.entered_at
        visitors_dict = {
            "who_entered": pas_name,
            "entered_at": time_when,
            'duration': time_inside
            }
        visitors_list.append(visitors_dict)

    non_closed_visits = visitors_list
    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
    


