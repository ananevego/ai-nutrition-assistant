from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()


def test_calculate():
    payload = {
        "weight": 80,
        "height": 180,
        "age": 30,
        "activity_level": "medium",
        "goal": "maintain",
    }

    response = client.post("/calculate", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "calories" in data
    assert "protein" in data
    assert "fat" in data
    assert "carbs" in data


def test_calculate_returns_expected_values():
    payload = {
        "weight": 80,
        "height": 180,
        "age": 30,
        "activity_level": "medium",
        "goal": "maintain",
    }

    response = client.post("/calculate", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "calories": 2759,
        "protein": 160,
        "fat": 64,
        "carbs": 386,
    }


def test_calculate_rejects_invalid_payload():
    payload = {
        "weight": -80,
        "height": 180,
        "age": 30,
        "activity_level": "medium",
        "goal": "maintain",
    }

    response = client.post("/calculate", json=payload)

    assert response.status_code == 422
