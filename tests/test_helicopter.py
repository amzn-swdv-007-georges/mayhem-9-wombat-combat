"""Activity: Live weather data dependency during a helicopter stunt.

The attack-helicopter flight team relies on real-time wind-speed
readings from the Australian Bureau of Meteorology (bom.gov.au)
before they can calculate a safe rotor-pitch angle.

These tests call the live :func:`~src.weather_api.get_live_wind_speed`
function directly.  The production implementation simulates an
unreachable external service, so the tests will fail until the
dependency is replaced.
"""

from unittest.mock import patch

from src.vehicles.helicopter import AttackHelicopter


def test_rotor_pitch_baseline_in_calm_wind() -> None:
    """In perfectly still air the rotor pitch should match the
    base angle of 8.0 degrees."""
    helicopter = AttackHelicopter("Crocodile-7")
    with patch("src.vehicles.helicopter.get_live_wind_speed", return_value=0.0):
        pitch = helicopter.calculate_rotor_pitch()
    assert pitch == 8.0


def test_rotor_pitch_increases_with_headwind() -> None:
    """A stronger headwind requires a steeper rotor pitch to
    maintain lift authority."""
    helicopter = AttackHelicopter("Crocodile-7")
    with patch("src.vehicles.helicopter.get_live_wind_speed", return_value=28.0):
        pitch = helicopter.calculate_rotor_pitch()
    assert pitch > 8.0


def test_severe_crosswind_requires_aggressive_pitch() -> None:
    """In severe crosswind conditions the rotor must bite harder."""
    helicopter = AttackHelicopter("Crocodile-7")
    with patch("src.vehicles.helicopter.get_live_wind_speed", return_value=28.0):
        pitch = helicopter.calculate_rotor_pitch()
    assert pitch > 12.0
