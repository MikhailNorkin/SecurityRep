from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import format_time
from django.shortcuts import get_object_or_404

# Функция проверяет на подозрительность сотрудника
def is_visit_long(visit_in_time , mins = 60 ):
    if visit_in_time > mins * 60:
        return True
    else:
        return False

# Функция возвращает ошибку, если карточка не найдена
def my_view(passcode):
    return get_object_or_404(Passcard, passcode = passcode)        

def passcard_info_view(request, passcode):
    
    # Программируем здесь

    # Задание 16. Вернуть ошибку 404
    my_view(passcode) 
    # Задание 16. Конец

    # Задание 12. Список всех посещений определенного посетителя
    myList = []
    passcard_visit = Passcard.objects.get(passcode = passcode)
    visits = Visit.objects.filter(passcard = passcard_visit)
    for visit_in in visits:
        delta = visit_in.leaved_at - visit_in.entered_at
        seconds = delta.total_seconds() 
        time_in = format_time(seconds)

        # Задание 15. Проверка на подозрительность
        time_inside = is_visit_long(seconds)
        # Задание 15. Конец

        myDict = {
            "entered_at": visit_in.entered_at,
            "duration": time_in,
            'is_strange': time_inside
            }
        myList.append(myDict)

    this_passcard_visits = myList
    context = {
        'passcard': passcard_visit,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
    # Задание 12. Конец
