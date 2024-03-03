from django.shortcuts import render
from .models import Cinema_events

def events_catalog1(request):
    events = Cinema_events.objects.exclude(title__isnull=True).exclude(title__exact='None inf')
    unique_events = list(set(events))
    return render(request, "cinema/index.html", {"events": unique_events})

def event_detail1(request, event_id):
    event = Cinema_events.objects.get(id=event_id)
    return render(request, 'cinema/event_details.html', {'event': event})