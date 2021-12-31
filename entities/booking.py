from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class Booking(BaseModel):
    id: int
    StartDate: datetime
    EndDate: datetime
    IsActive: bool
    CustomerId: int
    RoomId: int
