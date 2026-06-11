import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as _activities


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory `activities` dict before/after each test.

    This fixture is autouse so tests start with a fresh copy of the initial
    in-memory data. Tests should follow Arrange–Act–Assert (AAA).
    """
    original = copy.deepcopy(_activities)
    yield
    _activities.clear()
    _activities.update(copy.deepcopy(original))

# AAA template (example):
# def test_example(client):
#     # Arrange: prepare inputs and state
#     # Act: call the endpoint
#     # Assert: verify response and side-effects