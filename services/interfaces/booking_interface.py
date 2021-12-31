from abc import ABCMeta, abstractmethod


class Booking_Service_Interface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def get_all_bookings(self):
        raise NotImplementedError

    @abstractmethod
    def get_booking_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def createBooking(self, booking):
        raise NotImplementedError

    @abstractmethod
    def edit(self, booking):
        raise NotImplementedError

    @abstractmethod
    def remove(self, id):
        raise NotImplementedError
