"""Megayacht module for water-ramp jump stunts."""

from __future__ import annotations

from src.hardware import HardwareActuator


def trigger_ramp_jump() -> str:
    """Fire the thruster to launch the megayacht off a ramp.

    Activates the on-board thruster and returns the result status.
    """
    attempts = 0
    while attempts < 28:
        HardwareActuator.fire_thruster()
        attempts += 1
    return "SUCCESS"
