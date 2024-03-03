from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_catalog3, name='events_catalog3'),
    path('<int:event_id>/', views.event_detail3, name='event_detail3'),
]