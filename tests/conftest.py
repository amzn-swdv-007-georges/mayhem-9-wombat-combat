"""Shared fixtures for all test modules."""

import pytest
from src.environment import TrackEnvironment
from src.legacy import LegacyECUDriver


@pytest.fixture(autouse=True)
def reset_shared_state() -> None:
    """Reset shared global state after every test."""
    yield
    TrackEnvironment.reset()
    LegacyECUDriver._engine_running = False
    LegacyECUDriver._supercharger_active = False
