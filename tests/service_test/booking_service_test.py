from unittest import mock
from unittest.mock import patch

import pytest
from fastapi import HTTPException

from entities.booking import Booking
from entities.room import Room
from repos.implementations.booking_repo import Booking_Repo
from repos.implementations.room_repo import Room_Repo
from services.implementations.booking_service import Booking_Service

import datetime


# Patch. Object (class, Method)
# Then supply a return value to this class.
# Them execute a dependent method.
# This is mocking framework using unittest.mock. Which is an entirely diffrent framework but pytest encourages it.


# @patch('repos.implementations.booking_repo.Booking_Repo')
# @patch('repos.implementations.room_repo.Room_Repo')
# def test(MockClass1, MockClass2):
#   MockClass1.get_all_rooms.return_value = [Room(id=1, description='A')]
#  temp = Booking_Service(MockClass2,MockClass1).get_all_bookings()
#   assert temp == [Room(id=1, description='A')]


dateTimes = [
    (1, 1),
    (1, 2),
    (2, 2),
    (1, 5),
    (2, 10)
]

startDateInThePast = [(0), (-1), (-5)]
endDateDaysFromToday = [(0), (-1), (-5)]

StartDateBiggerThanEndDate = [
  (5, 1),
  (-10, -20),
  (5, -10),
  (3, -5)
]

@patch.object(Booking_Repo, 'get_all_bookings')
def test_BookingRepo_GetAll_ServiceGetsMockData(Booking_Repo_Mock):
    bookingReturn = [
        Booking(id=1, StartDate=datetime.datetime.now(), EndDate=datetime.datetime.now() + datetime.timedelta(days=14),
                IsActive=True, CustomerId=1,
                RoomId=1),
    ]
    Booking_Repo_Mock.return_value = bookingReturn

    tmp = Booking_Service().get_all_bookings()

    assert tmp == bookingReturn

@pytest.mark.parametrize("a,b", dateTimes)
@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_FindAvailableRoom_ValidDates_ExistingRoomId(Room_Repo_Mock, Booking_Repo_Mock, a, b):
    Booking_Repo_Mock.return_value = []
    Room_Repo_Mock.return_value = [Room(id=1, description='A'), Room(id=2, description='B')]
    startDate = datetime.datetime.now() + datetime.timedelta(days=a)
    endDate = datetime.datetime.now() + datetime.timedelta(days=b)
    tmp = Booking_Service().findAvailableRoom(startDate, endDate)
    assert tmp == 1


@pytest.mark.parametrize("a", startDateInThePast)
@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_FindAvailableRoom_StartDateInThePast_ThrowsArgumentException(Room_Repo_Mock, Booking_Repo_Mock, a):
    Booking_Repo_Mock.return_value = []
    Room_Repo_Mock.return_value = [Room(id=1, description='A'), Room(id=2, description='B')]
    startDate = datetime.datetime.now() + datetime.timedelta(days=a)
    endDate = startDate + datetime.timedelta(days=1)
    with pytest.raises(HTTPException) as e:
        tmp = Booking_Service().findAvailableRoom(startDate, endDate)
    assert e.value.status_code == 404
    assert e.value.detail == "The start date cannot be in the past or later than the end date."


@pytest.mark.parametrize("a", endDateDaysFromToday)
@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_FindAvailableRoom_EndDateInThePast_ThrowsArgumentException(Room_Repo_Mock, Booking_Repo_Mock, a):
    Booking_Repo_Mock.return_value = []
    Room_Repo_Mock.return_value = [Room(id=1, description='A'), Room(id=2, description='B')]
    endDate = datetime.datetime.now() + datetime.timedelta(days=a)
    startDate = endDate + datetime.timedelta(days=-1)

    with pytest.raises(HTTPException) as e:
        tmp = Booking_Service().findAvailableRoom(startDate, endDate)
    assert e.value.status_code == 404
    assert e.value.detail == "The start date cannot be in the past or later than the end date."


@pytest.mark.parametrize("a,b", dateTimes)
@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_GetFullyOccupiedDates_ValidDates_EmptyArray(Room_Repo_Mock, Booking_Repo_Mock, a, b):
    Booking_Repo_Mock.return_value = []
    Room_Repo_Mock.return_value = [Room(id=1, description='A'), Room(id=2, description='B')]
    startDate = datetime.datetime.now() + datetime.timedelta(days=a)
    endDate = datetime.datetime.now() + datetime.timedelta(days=b)
    tmp = Booking_Service().getFullyOccupiedDates(startDate, endDate)
    assert tmp == None

@pytest.mark.parametrize("a,b", StartDateBiggerThanEndDate)
@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_GetFullyOccupiedDates_StartDateBiggerThanEndDate_ThrowsArgumentException(Room_Repo_Mock, Booking_Repo_Mock, a, b):
    Booking_Repo_Mock.return_value = []
    Room_Repo_Mock.return_value = [Room(id=1, description='A'), Room(id=2, description='B')]
    startDate = datetime.datetime.now() + datetime.timedelta(days=a)
    endDate = datetime.datetime.now() + datetime.timedelta(days=b)
    with pytest.raises(HTTPException) as e:
        tmp = Booking_Service().getFullyOccupiedDates(startDate, endDate)
    assert e.value.status_code == 404
    assert e.value.detail == "The start date cannot be in the past or later than the end date."

@pytest.mark.parametrize("a,b", dateTimes)
@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_GetFullyOccupiedDates_ValidDates_ValidDates(Room_Repo_Mock, Booking_Repo_Mock, a, b):
    startDate = datetime.datetime.now() + datetime.timedelta(days=a)
    endDate = datetime.datetime.now() + datetime.timedelta(days=b)
    bookingReturn = [
        Booking(id=1, StartDate=datetime.datetime.now(), EndDate=datetime.datetime.now() + datetime.timedelta(days=14),
                IsActive=True, CustomerId=1,
                RoomId=1),
        Booking(id=2, StartDate=datetime.datetime.now(), EndDate=datetime.datetime.now() + datetime.timedelta(days=14),
                IsActive=True, CustomerId=1,
                RoomId=2),
    ]
    Booking_Repo_Mock.return_value = bookingReturn
    Room_Repo_Mock.return_value = [Room(id=1, description='A'), Room(id=2, description='B')]

    tmp = Booking_Service().getFullyOccupiedDates(startDate, endDate)
    assert tmp == None
