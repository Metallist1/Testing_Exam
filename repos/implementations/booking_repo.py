from repos.interfaces.booking_repo_interface import Booking_Repo_Interface
from repos.db.fake_db import get_booking_db


class Booking_Repo(Booking_Repo_Interface):

    def __init__(self):
        self.booking_table = get_booking_db()

    def get_all_bookings(self):
        return self.booking_table

    def get_booking_by_id(self, id):
        for i in range(len(self.booking_table)):
            if self.booking_table[i].id == id:
                return self.booking_table[i]
        return None

    def add(self, booking):
        self.booking_table.append(booking)
        return booking

    def edit(self, booking):
        for i in range(len(self.booking_table)):
            if self.booking_table[i].id == booking.id:
                self.booking_table[i] = booking
                return self.booking_table[i]
        return None

    def remove(self, id):
        for i in range(len(self.booking_table)):
            if self.booking_table[i].id == id:
                return self.booking_table.pop(i)
        return None



