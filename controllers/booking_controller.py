from fastapi import APIRouter, Depends, HTTPException

from dependencies import get_token_header
from entities.booking import Booking
from services.implementations.booking_service import Booking_Service

router = APIRouter(
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

booking_service = Booking_Service()


@router.get("/booking/", tags=["booking"])
async def get_all_bookings():
    return booking_service.get_all_bookings()


@router.get("/booking/{id}", tags=["booking"])
async def get_booking_by_id(id: int):
    if id > 0:
        return booking_service.get_booking_by_id(id)
    else:
        raise HTTPException(status_code=404, detail="Invalid ID")


@router.post(
    "/booking/",
    tags=["booking"],
    responses={403: {"description": "Operation forbidden"}},
)
async def create_booking(booking: Booking):
    if booking is None:
        raise HTTPException(status_code=404, detail="Invalid Booking")
    else:
        return booking_service.createBooking(booking)


@router.put(
    "/booking/{id}",
    tags=["booking"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_booking(id: int, item: Booking):
    if id > 0:
        booking = booking_service.get_booking_by_id(item.id)
        if booking is None:
            raise HTTPException(status_code=404, detail="Invalid ID")
        else:
            booking.CustomerId = item.CustomerId
            booking.IsActive = item.IsActive
            return booking_service.edit(booking)
    else:
        raise HTTPException(status_code=404, detail="Invalid ID")


@router.delete(
    "/booking/{id}",
    tags=["booking"],
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_booking(id: int):
    if id > 0:
        booking = booking_service.get_booking_by_id(id)
        if booking is None:
            raise HTTPException(status_code=404, detail="Invalid ID")
        else:
            return booking_service.remove(id)
    else:
        raise HTTPException(status_code=404, detail="Invalid ID")
