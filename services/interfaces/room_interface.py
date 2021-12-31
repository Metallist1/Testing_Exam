from abc import ABCMeta, abstractmethod


class Room_Service_Interface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def get_all_rooms(self):
        raise NotImplementedError

    @abstractmethod
    def get_room_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def delete_room(self, id):
        raise NotImplementedError
