from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about),
    path('child', views.child, name = 'child'),
]
