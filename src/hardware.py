"""Hardware abstraction layer for physical thruster actuators."""

from __future__ import annotations

from collections import deque

_firing_log: deque[float] = deque()


class HardwareActuator:
    """Controls a single physical thruster on a vehicle.

    Records every firing event in memory so tests can inspect
    actuation history without connecting to real hardware.
    """

    @staticmethod
    def fire_thruster() -> None:
        """Ignite the thruster and record the event."""
        _firing_log.append(1.0)

    @staticmethod
    def firing_count() -> int:
        """Return the total number of recorded thruster firings."""
        return len(_firing_log)

    @staticmethod
    def clear_firing_log() -> None:
        """Reset the firing history."""
        _firing_log.clear()
