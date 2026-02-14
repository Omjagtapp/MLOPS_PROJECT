import pytest
from fastapi.testclient import TestClient

from app.app import app  # app.py is copied into the container /app, tests import locally

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "ok"
    assert "model_loaded" in data


def test_predict_ok():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()

    # Validate response shape
    assert "prediction" in data
    assert "probabilities" in data
    assert "model_version" in data

    assert isinstance(data["prediction"], str)
    assert isinstance(data["probabilities"], list)
    assert len(data["probabilities"]) == 3
    assert all(isinstance(x, (int, float)) for x in data["probabilities"])


def test_predict_validation_error():
    # Missing required fields should trigger FastAPI/Pydantic validation
    r = client.post("/predict", json={"sepal_length": 5.1})
    assert r.status_code == 422
