from django.shortcuts import render
from .models import Theatre_events

def events_catalog2(request):
    events = Theatre_events.objects.exclude(title__isnull=True).exclude(title__exact='None inf')
    unique_events = list(set(events))
    return render(request, "theatre/index.html", {"events": unique_events})

def event_detail2(request, event_id):
    event = Theatre_events.objects.get(id=event_id)
    return render(request, 'theatre/event_details.html', {'event': event})