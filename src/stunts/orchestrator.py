"""Stunt orchestrator that coordinates multiple vehicles for a climax sequence."""

from __future__ import annotations

from typing import Any

from src.environment import TrackEnvironment
from src.finance import get_engine_temperature, wire_insurance_funds
from src.hardware import HardwareActuator
from src.vehicles.helicopter import AttackHelicopter
from src.vehicles.interceptor import Interceptor
from src.vehicles.megayacht import trigger_ramp_jump
from src.vehicles.truck import MonsterTruck


def execute_climax_stunt() -> dict[str, Any]:
    """Run the full climax stunt sequence across all vehicles.

    Coordinates the monster truck launch, helicopter rotor
    adjustment, megayacht ramp jump, and interceptor shutdown.
    Transfers insurance funds and records engine temperature
    for post-stunt reporting.

    Returns:
        A summary dictionary containing the result of each
        vehicle's action and auxiliary telemetry.
    """
    TrackEnvironment.reset()

    wire_insurance_funds(
        amount=500_000.00,
        recipient="Stunt Unit Alpha",
        reference="CLIMAX-001",
    )

    truck = MonsterTruck("Grave Digger")
    truck_result = truck.perform_launch()

    helicopter: AttackHelicopter | None = None
    rotor_pitch: float | None = None
    try:
        helicopter = AttackHelicopter("Apache-1")
        rotor_pitch = helicopter.calculate_rotor_pitch()
    except ConnectionError:
        rotor_pitch = None

    megayacht_result = trigger_ramp_jump()

    interceptor = Interceptor("Pursuit-1")
    interceptor.engage_pursuit_mode()
    interceptor_shutdown = interceptor.shutdown()

    thruster_firings = HardwareActuator.firing_count()
    HardwareActuator.clear_firing_log()

    engine_temp = get_engine_temperature()

    return {
        "truck": {
            "vehicle": truck.name,
            "result": truck_result,
            "friction": TrackEnvironment.friction_coefficient,
        },
        "helicopter": {
            "vehicle": helicopter.name if helicopter else None,
            "rotor_pitch": rotor_pitch,
        },
        "megayacht": {
            "result": megayacht_result,
            "thruster_firings": thruster_firings,
        },
        "interceptor": {
            "vehicle": interceptor.name,
            "shutdown_engine_was_running": interceptor_shutdown,
        },
        "telemetry": {
            "engine_temperature_c": engine_temp,
        },
    }
