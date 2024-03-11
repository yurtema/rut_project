from django.shortcuts import render
from .models import Cinema_events

def events_catalog1(request):
    events = Cinema_events.objects.all()
    for event in events:
        if event.images:
            event.first_images = event.images[0]
    return render(request, "cinema/index.html", {"events": events})

def event_detail1(request, event_id):
    event = Cinema_events.objects.get(id=event_id)
    return render(request, 'cinema/event_details.html', {'event': event})
