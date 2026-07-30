"""Activity: Behaviour verification with mocks.

The megayacht stunt team fires a thruster to launch off a water
ramp.  The test must verify the thruster fires **exactly once**,
not just check the return value — because a bug in the production
code causes 28 firings instead of 1.
"""

from unittest.mock import patch

from src.vehicles.megayacht import trigger_ramp_jump


def test_thruster_fires_exactly_once_during_ramp_jump() -> None:
    """The ramp-jump sequence must fire the thruster exactly once."""
    with patch("src.vehicles.megayacht.HardwareActuator") as mock_actuator:
        result = trigger_ramp_jump()

    assert result == "SUCCESS"
    mock_actuator.fire_thruster.assert_called_once()
