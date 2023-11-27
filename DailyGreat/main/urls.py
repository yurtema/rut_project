from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('child', views.child, name = 'child'),
    path('cinema', views.cinema, name = 'cinema'),
    path('theatre', views.theatre, name = 'theatre'),
    path('exhibition', views.exhibition, name = 'exhibition'),
    path('concert', views.concert, name = 'concert'),
    path('other', views.other, name = 'other'),
    path('calendar', views.calendar, name = 'calendar'),
]
