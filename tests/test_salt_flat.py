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


# Solution: An autouse fixture runs before and after every test in this module.
# The code before yield is setup; the code after yield is teardown (always runs,
# even if the test raises). This guarantees TrackEnvironment always starts
# fresh — eliminating the order-dependent failure.
@pytest.fixture(autouse=True)
def reset_track_environment() -> None:
    """Restore default track conditions before and after each test."""
    TrackEnvironment.reset()
    yield
    TrackEnvironment.reset()


# Independent: starts with a clean, dry track (friction_coefficient = 0.85).
# The autouse fixture guarantees this regardless of what earlier tests did.
def test_truck_launches_on_dry_surface() -> None:
    """A truck should launch when the track has normal grip."""
    truck = MonsterTruck("Salt Rattler")
    assert truck.can_launch() is True
    result = truck.perform_launch()
    assert result == "LAUNCHED"


# Safe to mutate: the autouse fixture resets the coefficient back to 0.85
# after this test finishes, so no other test sees the 0.1 spill value.
def test_oil_spill_makes_launch_unsafe() -> None:
    """Spilled oil reduces friction below the safe-launch threshold."""
    TrackEnvironment.set_oil_slick()
    truck = MonsterTruck("Salt Rattler")
    assert truck.can_launch() is False
    result = truck.perform_launch()
    assert result == "ABORTED"


# No longer order-dependent: the autouse fixture ensures friction_coefficient
# is 0.85 before this test runs, even if test_oil_spill_makes_launch_unsafe
# ran first. The "ghost in the machine" is exorcised.
def test_crew_repairs_truck_and_re_checks_track() -> None:
    """After an aborted launch the crew inspects the surface again.

    They expect the surface to be dry — but a previous test may
    have left an oil slick behind because nobody cleaned it up.
    """
    truck = MonsterTruck("Salt Rattler")
    assert truck.can_launch() is True
    result = truck.perform_launch()
    assert result == "LAUNCHED"
