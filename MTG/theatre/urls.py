from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_catalog2, name='events_catalog2'),
    path('<int:event_id>/', views.event_detail2, name='event_detail2'),
]