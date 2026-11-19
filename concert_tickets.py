# === Stage 1: Каркас модуля ===
# Project: ConcertTickets
import datetime

class ConcertTicket:
    def __init__(self, artist, venue, date, price):
        self.artist = artist
        self.venue = venue
        self.date = date
        self.price = price

    def __str__(self):
        return f"Билет: {self.artist} в {self.venue}, {self.date}, {self.price} руб."

def create_demo_records():
    return [
        ConcertTicket("Группа A", "Площадка 1", datetime.date(2024, 6, 15), 1500),
        ConcertTicket("Артист B", "Площадка 2", datetime.date(2024, 7, 20), 2000),
        ConcertTicket("Бэнд C", "Площадка 3", datetime.date(2024, 8, 25), 1000),
    ]

def main():
    tickets = create_demo_records()
    for ticket in tickets:
        print(ticket)

if __name__ == "__main__":
    main()
