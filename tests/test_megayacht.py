"""Activity: State verification instead of behaviour verification.

The megayacht stunt team fires a thruster to launch off a water
ramp.  The test only checks the **return value** of the launch
function and never inspects how many times the thruster was
actually fired.

This means the test passes even though a production bug causes
the thruster to fire 28 times instead of once — a catastrophic
overload that would destroy a real actuator.
"""

from src.hardware import HardwareActuator
from src.vehicles.megayacht import trigger_ramp_jump


def test_megayacht_clears_the_ramp() -> None:
    """The ramp-jump sequence completes and reports success."""
    HardwareActuator.clear_firing_log()
    result = trigger_ramp_jump()
    assert result == "SUCCESS"
