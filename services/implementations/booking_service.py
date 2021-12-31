import pytz as pytz
from fastapi import HTTPException

from entities.booking import Booking
from repos.implementations.booking_repo import Booking_Repo
from repos.implementations.room_repo import Room_Repo
from services.interfaces.booking_interface import Booking_Service_Interface
import datetime

utc = pytz.UTC


class Booking_Service(Booking_Service_Interface):

    def __init__(self):
        self.booking_repo = Booking_Repo()
        self.room_repo = Room_Repo()

    def get_all_bookings(self):
        return self.booking_repo.get_all_bookings()

    def get_booking_by_id(self, id):
        return self.booking_repo.get_booking_by_id(id)

    def createBooking(self, booking):
        roomId = self.findAvailableRoom(booking.StartDate, booking.EndDate)
        if roomId >= 0:
            booking.RoomId = roomId
            booking.IsActive = True
            return self.booking_repo.add(booking)
        else:
            raise HTTPException(status_code=404,
                                detail="No available room")

    def edit(self, booking):
        return self.booking_repo.edit(booking)

    def remove(self, id):
        return self.booking_repo.remove(id)

    def findAvailableRoom(self, startDate, endDate):
        startDate = self.parseTime(startDate)
        endDate = self.parseTime(endDate)

        checked_on = self.parseTime(datetime.datetime.now())

        if startDate <= checked_on or startDate > endDate:
            raise HTTPException(status_code=404,
                                detail="The start date cannot be in the past or later than the end date.")
        activeBookings = self.getActiveBookings(self.booking_repo.get_all_bookings())
        allRooms = self.room_repo.get_all_rooms()
        for i in range(len(allRooms)):
            shouldBeSelected = True

            allActiveBookingsForRoom = self.getActiveBookingsByRoom(activeBookings, allRooms[i])
            if all([(startDate < self.parseTime(x.StartDate) and
                     endDate < self.parseTime(x.StartDate) or
                     startDate > self.parseTime(x.EndDate) and
                     endDate > self.parseTime(x.EndDate)) for x in allActiveBookingsForRoom]):
                return allRooms[i].id
        return -1

    def parseTime(self, timeDate):
        table_expired_date = timeDate + datetime.timedelta(minutes=10)
        startDate = table_expired_date.replace(tzinfo=utc)
        return startDate

    def getFullyOccupiedDates(self, startDate, endDate):
        if startDate > endDate:
            raise HTTPException(status_code=404,
                                detail="The start date cannot be in the past or later than the end date.")

    def getActiveBookings(self, listOfBookings):
        newList = []
        for i in range(len(listOfBookings)):
            if listOfBookings[i].IsActive:
                newList.append(listOfBookings[i])
        return newList

    def getActiveBookingsByRoom(self, listOfBookings, roomId):
        newList = []
        for i in range(len(listOfBookings)):
            if listOfBookings[i].RoomId == roomId.id:
                newList.append(listOfBookings[i])
        return newList
