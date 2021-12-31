from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# Booking token test
def test_GetAllBookings_BadToken_ReturnsException():
    response = client.get(
        "/booking/?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_GetSingleBooking_BadToken_ReturnsException():
    response = client.get(
        "/booking/1?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_CreateBooking_BadToken_ReturnsException():
    response = client.post(
        "/booking/?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_UpdateBooking_BadToken_ReturnsException():
    response = client.put(
        "/booking/1?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_DeleteBooking_BadToken_ReturnsException():
    response = client.delete(
        "/booking/1?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


# Booking header token test

def test_GetAllBookings_BadHeaderToken_ReturnsException():
    response = client.get(
        "/booking/?token=super_token",
        headers={"X-Token": "bad_token"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}


def test_GetSingleBooking_BadHeaderToken_ReturnsException():
    response = client.get(
        "/booking/1?token=super_token",
        headers={"X-Token": "bad_token"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}


def test_CreateBooking_BadHeaderToken_ReturnsException():
    response = client.post(
        "/booking/?token=bad_token",
        headers={"X-Token": "bad_token"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_UpdateBooking_BadHeaderToken_ReturnsException():
    response = client.put(
        "/booking/1?token=bad_token",
        headers={"X-Token": "bad_token"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_DeleteBooking_BadHeaderToken_ReturnsException():
    response = client.delete(
        "/booking/1?token=super_token",
        headers={"X-Token": "bad_token"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "X-Token header invalid"}
