from fastapi import APIRouter, HTTPException

from services.implementations.room_service import Room_Service

router = APIRouter()

room_service = Room_Service()

@router.get("/room/", tags=["room"])
async def read_all_rooms():
    return room_service.get_all_rooms()


@router.get("/room/{id}", tags=["room"])
async def get_room_by_id(id: int):
    room = room_service.get_room_by_id(id)
    if room is None:
        raise HTTPException(status_code=404, detail="Invalid Room")
    else:
        return room


@router.delete("/room/{id}", tags=["room"])
async def delete_room(id: int):
    if id > 0:
        return room_service.delete_room(id)
    else:
        raise HTTPException(status_code=404, detail="Invalid ID")
