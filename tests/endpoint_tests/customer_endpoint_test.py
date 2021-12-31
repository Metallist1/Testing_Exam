from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# In-case you cant run Pytest. Use : python -m pytest
# Unit test to test out Token responses. Can be used to test out output as well.
def test_GetAllCustomers_BadToken_ReturnsException():
    response = client.get(
        "/customer/?token=bad_token",
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "No token provided"}
