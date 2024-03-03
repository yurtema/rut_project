from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_catalog1, name='events_catalog1'),
    path('<int:event_id>/', views.event_detail1, name='event_detail1'),
]
