from django.shortcuts import render
from .models import Cinema_events

def events_catalog1(request):
    events = Cinema_events.objects.all()
    for event in events:
        if event.images:
            event.urls_list = event.images[1:-1]
            event.new_name = event.title[:30]
            event.first_images = event.urls_list.strip("[]").split(", ")[0][1:-1]
    return render(request, "cinema/index.html", {"events": events})

def event_detail1(request, event_id):
    event = Cinema_events.objects.get(id=event_id)
    event.urls_list = event.images[1:-1]
    event.first_image = event.urls_list.strip("[]").split(", ")[0][1:-1]
    return render(request, 'cinema/event_details.html', {'event': event})
