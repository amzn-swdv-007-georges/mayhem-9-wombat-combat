"""Shared fixtures for all test modules."""

import pytest
from src.environment import TrackEnvironment


@pytest.fixture(autouse=True)
def reset_track_environment() -> None:
    yield
    TrackEnvironment.reset()
