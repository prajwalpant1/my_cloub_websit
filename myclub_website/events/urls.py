
from asyncio import events
from unicodedata import name
from django import views
from django.urls import path,include

from . import views

urlpatterns = [
     path('',
     views.home,name='home'),
 
path('<int:year>/<str:month>/',views.home,name='home'),
path('events',views.all_events,name='list_events'),
]