import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_app_exists():
    assert app is not None


def test_app_is_flask():
    assert app.name == "app"
