from repos.db.fake_db import get_room_db
from repos.interfaces.room_repo_interface import Room_Repo_Interface


class Room_Repo(Room_Repo_Interface):

    def __init__(self):
        self.room_table = get_room_db()

    def get_all_rooms(self):
        return self.room_table

    def get_room_by_id(self, id):
        for i in range(len(self.room_table)):
            if self.room_table[i].id == id:
                return self.room_table[i]
        return None

    def delete_room(self, id):
        for i in range(len(self.room_table)):
            if self.room_table[i].id == id:
                return self.room_table.pop(i)
        return None
