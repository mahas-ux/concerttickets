# === Stage 4: Удаление и восстановление ===
# Project: ConcertTickets
import datetime

class SoftDeletedTicket:
    def __init__(self, artist, venue, date, price, is_deleted=False):
        self.artist = artist
        self.venue = venue
        self.date = date
        self.price = price
        self.is_deleted = is_deleted

    def restore(self):
        self.is_deleted = False
        return self

    def soft_delete(self):
        self.is_deleted = True
        return self

    def __str__(self):
        status = "удалён" if self.is_deleted else "активен"
        return f"Билет: {self.artist} в {self.venue}, {self.date}, {self.price} руб. [{status}]"


class TicketRepository:
    def __init__(self):
        self._tickets = []
        self._deleted_tickets = []

    def add_ticket(self, ticket):
        self._tickets.append(ticket)
        return ticket

    def get_all_active(self):
        return [t for t in self._tickets if not t.is_deleted]

    def get_by_id(self, index, active_only=True):
        if active_only:
            tickets = self._tickets
        else:
            tickets = self._tickets + self._deleted_tickets
        if 0 <= index < len(tickets):
            return tickets[index]
        return None

    def delete_ticket(self, index):
        ticket = self.get_by_id(index, active_only=True)
        if ticket is None:
            return False
        self._tickets.remove(ticket)
        self._deleted_tickets.append(ticket)
        return True

    def restore_ticket(self, index, active_only=False):
        ticket = self.get_by_id(index, active_only=active_only)
        if ticket is None:
            return False
        if ticket in self._deleted_tickets:
            self._deleted_tickets.remove(ticket)
        ticket.restore()
        return True

    def get_deleted_tickets(self):
        return list(self._deleted_tickets)

    def __len__(self):
        return len(self._tickets)


def demo():
    repo = TicketRepository()
    repo.add_ticket(SoftDeletedTicket("Pink Floyd", "Kronstadt", datetime.date(2025, 6, 1), 4500))
    repo.add_ticket(SoftDeletedTicket("Muse", "Armeecinema", datetime.date(2025, 7, 15), 3200))
    repo.add_ticket(SoftDeletedTicket("Daft Punk", "Kronstadt", datetime.date(2025, 8, 20), 5100))

    print("Активные билеты:", len(repo.get_all_active()))
    repo.delete_ticket(1)
    print("После удаления: активных:", len(repo.get_all_active()))
    print("В корзине:", repo.get_deleted_tickets()[0])
    repo.restore_ticket(1, active_only=False)
    print("После восстановления: активных:", len(repo.get_all_active()))


if __name__ == "__main__":
    demo()
