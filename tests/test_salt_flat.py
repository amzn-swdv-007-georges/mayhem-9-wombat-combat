"""Activity: Lingering global state on the Bonneville Salt Flats.

A monster-truck team is preparing for a land-speed-record ramp jump
on the salt flats.  The track crew accidentally spills oil during
setup and does **not** clean the surface afterwards.

Running these tests in a different order can produce different
results because the oil-spill test contaminates the shared
:class:`TrackEnvironment` state and never restores it.
"""

import pytest

from src.environment import TrackEnvironment
from src.vehicles.truck import MonsterTruck


# Reset the shared TrackEnvironment state before every test so that
# mutations in one test never leak into the next.
@pytest.fixture(autouse=True)
def reset_track() -> None:
    TrackEnvironment.reset()


# Default dry surface — truck has full grip and launches successfully.
def test_truck_launches_on_dry_surface() -> None:
    """A truck should launch when the track has normal grip."""
    truck = MonsterTruck("Salt Rattler")
    assert truck.can_launch() is True
    result = truck.perform_launch()
    assert result == "LAUNCHED"


# Spilled oil reduces friction below the safe-launch threshold.
def test_oil_spill_makes_launch_unsafe() -> None:
    """Spilled oil reduces friction below the safe-launch threshold."""
    TrackEnvironment.friction_coefficient = 0.1
    truck = MonsterTruck("Salt Rattler")
    assert truck.can_launch() is False
    result = truck.perform_launch()
    assert result == "ABORTED"


# After the oil-spill test, the fixture resets the track to dry
# conditions, so this test sees a clean surface and launches safely.
def test_crew_repairs_truck_and_re_checks_track() -> None:
    """After an aborted launch the crew inspects the surface again.

    They expect the surface to be dry — but a previous test may
    have left an oil slick behind because nobody cleaned it up.
    """
    truck = MonsterTruck("Salt Rattler")
    assert truck.can_launch() is True
    result = truck.perform_launch()
    assert result == "LAUNCHED"
