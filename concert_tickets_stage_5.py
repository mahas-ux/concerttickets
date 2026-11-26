# === Stage 5: Связанная сущность ===
# Project: ConcertTickets
event.py

import datetime
from concerttickets.domain.event import Event, EventError


def add_event(name, venue, city, start_datetime):
    """Создаёт и сохраняет новое событие."""
    if not name or not venue or not city:
        raise EventError("Имя, площадка и город обязательны для события.")
    if start_datetime is None or start_datetime <= datetime.datetime.now():
        raise EventError("Дата старта события должна быть в будущем.")

    event = Event(
        id=generate_event_id(),
        name=name,
        venue=venue,
        city=city,
        start_datetime=start_datetime,
    )
    EVENT_STORE.append(event)
    return event


def get_event(event_id):
    """Возвращает событие по идентификатору или None."""
    for event in EVENT_STORE:
        if event.id == event_id:
            return event
    return None


def find_event_by_venue(venue):
    """Возвращает список событий, проходящих в указанной площадке."""
    return [event for event in EVENT_STORE if event.venue == venue]


def find_events_on_date(day):
    """Возвращает события, начинающиеся в указанную дату (день)."""
    if day is None:
        return []
    return [
        event
        for event in EVENT_STORE
        if event.start_datetime.date() == day
    ]


def generate_event_id():
    """Формирует уникальный идентификатор события."""
    counter = 1
    for event in EVENT_STORE:
        counter = max(counter, event.id)
    return counter


EVENT_STORE = []
