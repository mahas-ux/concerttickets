# === Stage 3: Хранилище в памяти ===
# Project: ConcertTickets
in_memory_tickets.py

from datetime import date


class Ticket:
    def __init__(self, ticket_id, artist, venue, show_date, price):
        self.ticket_id = ticket_id
        self.artist = artist
        self.venue = venue
        self.show_date = show_date
        self.price = price

    def __repr__(self):
        return "Ticket(id={0}, artist={1}, venue={2}, show_date={3}, price={4})".format(
            self.ticket_id, self.artist, self.venue, self.show_date, self.price)


class InMemoryTicketStore:
    def __init__(self):
        self._tickets = {}

    def add_ticket(self, ticket):
        if ticket.ticket_id in self._tickets:
            raise ValueError("Ticket with id {0} already exists".format(ticket.ticket_id))
        self._tickets[ticket.ticket_id] = ticket

    def get_ticket(self, ticket_id):
        return self._tickets.get(ticket_id)

    def list_tickets(self):
        return list(self._tickets.values())


if __name__ == "__main__":
    store = InMemoryTicketStore()
    store.add_ticket(Ticket(1, "The Beatles", "O2 Arena", date(2025, 6, 15), 2500))
    store.add_ticket(Ticket(2, "ABBA", "Palau de la Música", date(2025, 7, 20), 3000))
    for t in store.list_tickets():
        print(t)
    print(store.get_ticket(2))
    print(store.get_ticket(999))
