from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

DeleteRoom = [
    ("-1", {"detail": "Invalid ID"}),
    ("0", {"detail": "Invalid ID"}),
]

GetSingleRoom = [
    ("-1", {"detail": "Invalid Room"}),
    ("0", {"detail": "Invalid Room"}),
]


@pytest.mark.parametrize("a,expected", DeleteRoom)
def test_DeleteRoom_BadID_ReturnsException(a, expected):
    response = client.delete(
        "/room/" + a + "?token=super_token",
    )
    assert response.status_code == 404
    assert response.json() == expected


@pytest.mark.parametrize("a,expected", GetSingleRoom)
def test_GetSingleRoom_BadID_ReturnsException(a, expected):
    response = client.get(
        "/room/" + a + "?token=super_token",
    )
    assert response.status_code == 404
    assert response.json() == expected
