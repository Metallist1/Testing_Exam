from unittest import mock
from unittest.mock import patch

import pytest

from entities.booking import Booking
from entities.room import Room
from repos.implementations.booking_repo import Booking_Repo
from repos.implementations.room_repo import Room_Repo
from services.implementations.booking_service import Booking_Service

import datetime

date = datetime.datetime.now() + datetime.timedelta(days=4)


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

@patch.object(Booking_Repo, 'get_all_bookings')
def test_BookingRepo_GetAll_ServiceGetsMockData(Booking_Repo_Mock):
    bookingReturn = [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1,
                RoomId=1),
    ]
    Booking_Repo_Mock.return_value = bookingReturn

    tmp = Booking_Service().get_all_bookings()

    assert tmp == bookingReturn


"""
@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_fo(Room_Repo_Mock, Booking_Repo_Mock):
#    MockClass1.return_value = 1
    Room_Repo_Mock.return_value = [Room(id=1, description='A')]
    Booking_Repo.return_value = [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]
    tmp = Booking_Service().get_all_bookings()
    assert tmp == [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]


@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_fo(Room_Repo_Mock, Booking_Repo_Mock):
#    MockClass1.return_value = 1
    Room_Repo_Mock.return_value = [Room(id=1, description='A')]
    Booking_Repo.return_value = [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]
    tmp = Booking_Service().get_all_bookings()
    assert tmp == [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]


@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_fo(Room_Repo_Mock, Booking_Repo_Mock):
#    MockClass1.return_value = 1
    Room_Repo_Mock.return_value = [Room(id=1, description='A')]
    Booking_Repo.return_value = [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]
    tmp = Booking_Service().get_all_bookings()
    assert tmp == [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]


@patch.object(Booking_Repo, 'get_all_bookings')
@patch.object(Room_Repo, 'get_all_rooms')
def test_fo(Room_Repo_Mock, Booking_Repo_Mock):
#    MockClass1.return_value = 1
    Room_Repo_Mock.return_value = [Room(id=1, description='A')]
    Booking_Repo.return_value = [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]
    tmp = Booking_Service().get_all_bookings()
    assert tmp == [
        Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    ]
    
"""
