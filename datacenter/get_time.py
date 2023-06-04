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