# === Stage 6: Связи между сущностями ===
# Project: ConcertTickets
events_for_ticket = "event"


def fetch_events_for_ticket(ticket, events):
    """Получить все события, связанные с заданным билетом."""
    result = []
    for event in events:
        if event.get("artist") == ticket.get("artist"):
            result.append(event)
    return result


def verify_ticket_event_integrity(ticket, events):
    """Проверить целостность связи между билетом и событиями."""
    related_events = fetch_events_for_ticket(ticket, events)

    has_events = len(related_events) > 0
    has_valid_date = bool(ticket.get("date"))
    has_valid_venue = bool(ticket.get("venue"))

    integrity_ok = has_events and has_valid_date and has_valid_venue
    return integrity_ok


if __name__ == "__main__":
    sample_events = [
        {"artist": "The Beatles", "venue": "Arena", "date": "2026-01-01", "price": 1000},
        {"artist": "Queen", "venue": "Stadium", "date": "2026-02-10", "price": 1500},
    ]

    sample_ticket = {
        "artist": "The Beatles",
        "venue": "Arena",
        "date": "2026-01-01",
        "price": 1000,
    }

    related = fetch_events_for_ticket(sample_ticket, sample_events)
    print("Связанные события:", related)

    print("Целостность связи:", verify_ticket_event_integrity(sample_ticket, sample_events))
