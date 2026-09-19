import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200  # nosec B101

    data = response.get_json()

    assert data["message"] == "Welcome to My Page, Greetings by Hamza"
    assert data["platform"] == "GitHub Actions"
    assert data["runtime"] == "Docker + Flask"


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200  # nosec B101

    data = response.get_json()

    assert data["status"] == "healthy"
