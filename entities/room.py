from pydantic import BaseModel


class Room(BaseModel):
    id: int
    description: str
