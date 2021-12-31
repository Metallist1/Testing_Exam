from entities.room import Room
from entities.customer import Customer
from entities.booking import Booking
import datetime

date = datetime.datetime.now() + datetime.timedelta(days=4)

fake_customer_db = [Customer(id=1, name='John Smith', email='js@gmail.com'),
                    Customer(id=2, name='Jane Doe', email='jd@gmail.com')]

fake_booking_db = [
    Booking(id=1, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=1),
    Booking(id=2, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=2, RoomId=2),
    Booking(id=3, StartDate=date, EndDate=date + datetime.timedelta(days=14), IsActive=True, CustomerId=1, RoomId=3), ]

fake_room_db = [Room(id=1, description='A'), Room(id=2, description='B'), Room(id=3, description='C')]


def get_customer_db():
    return fake_customer_db


def get_booking_db():
    return fake_booking_db


def get_room_db():
    return fake_room_db
