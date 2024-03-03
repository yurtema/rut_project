from django.db.models import Count

import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MTG.settings')
django.setup()

from cinema.models import Cinema_events
from theatre.models import Theatre_events
from concert.models import Concert_events

check_arr = []
#Cinema
# def load_data_to_db_cinema():
#     json_dir = 'D:/PythonProject/data1j'
#     for filename in os.listdir(json_dir):
#         if filename.endswith(".json"):
#             with open(os.path.join(json_dir, filename), 'r', encoding='utf-8') as file:
#                 event_data = json.load(file)
#                 if event_data['Название'] not in check_arr:
#                     check_arr.append(event_data['Название'])
#                     event = Cinema_events(
#                         # title = event_data.get("Название"),
#                         # description = event_data.get("Описание"),
#                         # afisha = event_data.get("О фильме"),
#                         # author = event_data.get("Режиссёр"),
#                         # participants = event_data.get("В ролях"),
#                         # time = event_data.get("Время"),
#                         # city = event_data.get("Страна"),
#                         # year = event_data.get("Год производства"),
#                         # original_name = event_data.get("Оригинальное название"),
#                         poster = event_data.get("Постер"),
#                         images = event_data.get("Изображения")
#                     )
#                 event.save()
# load_data_to_db_cinema()
#
# Cinema_events.objects.filter(title="None inf").delete()

#Theatre
def load_to_db_theatre():
    json_dir = 'D:/PythonProject/data2j'
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            with open(os.path.join(json_dir, filename), 'r', encoding='utf-8') as file:
                event_data = json.load(file)
                if event_data['Название'] not in check_arr:
                    check_arr.append(event_data['Название'])
                    event = Theatre_events(
                        title = event_data.get('Название'),
                        afisha = event_data.get('О фильме'),
                        description = event_data.get('Описание'),
                        images = event_data.get('Изображения'),
                        customer = event_data.get('Театр-постановщик'),
                        participants = event_data.get('В ролях'),
                        author = event_data.get('Режиссер'),
                        time = event_data.get('Время')
                    )
                event.save()
load_to_db_theatre()

#Concert

# def load_to_db_concert():
#     json_dir = 'D:/PythonProject/data3j'
#     for filename in os.listdir(json_dir):
#         if filename.endswith('.json'):
#             with open(os.path.join(json_dir, filename), 'r', encoding='utf-8') as file:
#                 event_data = json.load(file)
#                 if event_data['Название'] not in check_arr:
#                     check_arr.append(event_data['Название'])
#                     event = Concert_events(
#                         title = event_data.get('Название'),
#                         afisha = event_data.get('О фильме'),
#                         description = event_data.get('Описание'),
#                         images = event_data.get('Изображения')
#                     )
#                 event.save()
# load_to_db_concert()





#
# duplicate_titles = Event.objects.values('title').annotate(count=Count('title')).filter(count__gt=1)
#
# for item in duplicate_titles:
#     Event.objects.filter(title=item['title']).delete()