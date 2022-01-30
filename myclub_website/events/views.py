from time import time
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import date, datetime
from .models import Event
# Create your views here.



def all_events(request):
    events=Event.objects.all()
    return render(request,'events/event_lists.html',{'events':events})


def home(request , year=datetime.now().year, month=datetime.now().strftime('%B')):
    name='prajwal'
    month=month.capitalize()
    #convert month to number
    month_number=list(calendar.month_name).index(month)
    month_number=int(month_number)
    #create a calender
    cal=HTMLCalendar().formatmonth(year,month_number)
    now=datetime.now()
    courent_year=now.year

    time=now.strftime('%I:%M:%S %p')

    return render(request,'events/home.html',{
        'name':name,
        'year':year,
        'month':month,
        'month_number':month_number,
        'cal':cal,
        'courent_year':courent_year,
        'time':time,
    })