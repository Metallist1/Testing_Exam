from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Room token test
def test_GetAllRooms_BadToken_ReturnsException():
    response = client.get(
        "/room/?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_GetSingleRoom_BadToken_ReturnsException():
    response = client.get(
        "/room/1?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}


def test_DeleteRoom_BadToken_ReturnsException():
    response = client.delete(
        "/room/1?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}

