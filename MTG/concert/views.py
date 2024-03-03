from django.shortcuts import render
from .models import Concert_events

def events_catalog3(request):
    events = Concert_events.objects.exclude(title__isnull=True).exclude(title__exact='None inf')
    unique_events = list(set(events))
    return render(request, "concert/index.html", {"events": unique_events})

def event_detail3(request, event_id):
    event = Concert_events.objects.get(id=event_id)
    return render(request, 'concert/event_details.html', {'event': event})