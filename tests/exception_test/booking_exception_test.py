from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)

InvalidIds = [
    ("-1", {"detail": "Invalid ID"}),
    ("0", {"detail": "Invalid ID"}),
]


@pytest.mark.parametrize("a,expected", InvalidIds)
def test_DeleteBooking_BadID_ReturnsException(a, expected):
    response = client.delete(
        "/booking/" + a + "?token=super_token",
        headers={"X-Token": "super_secret_token"},
    )
    assert response.status_code == 404
    assert response.json() == expected


@pytest.mark.parametrize("a,expected", InvalidIds)
def test_GetSingleBooking_BadID_ReturnsException(a, expected):
    response = client.get(
        "/booking/" + a + "?token=super_token",
        headers={"X-Token": "super_secret_token"},
    )
    assert response.status_code == 404
    assert response.json() == expected


@pytest.mark.parametrize("a,expected", InvalidIds)
def test_UpdateSingleBooking_BadID_ReturnsException(a, expected):
    response = client.put(
        "/booking/" + a + "?token=super_token",
        headers={"X-Token": "super_secret_token"},
        json={"id": 0,"StartDate": "2021-12-31T21:10:19.882Z","EndDate": "2021-12-31T21:10:19.882Z","IsActive": True,"CustomerId": 0,"RoomId": 0},
    )
    assert response.status_code == 404
    assert response.json() == expected


def test_UpdateSingleBooking_BadBooking_ReturnsException():
    response = client.put(
        "/booking/1?token=super_token",
        headers={"X-Token": "super_secret_token"},
        json={"id": 0, "StartDate": "2021-12-31T21:10:19.882Z", "EndDate": "2021-12-31T21:10:19.882Z", "IsActive": True,
              "CustomerId": 0, "RoomId": 0},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Invalid ID"}
