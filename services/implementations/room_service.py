from repos.implementations.room_repo import Room_Repo
from services.interfaces.room_interface import Room_Service_Interface


class Room_Service(Room_Service_Interface):

    def __init__(self):
        self.room_repo = Room_Repo()

    def get_all_rooms(self):
        return self.room_repo.get_all_rooms()

    def get_room_by_id(self, id):
        return self.room_repo.get_room_by_id(id)

    def delete_room(self, id):
        return self.room_repo.delete_room(id)


