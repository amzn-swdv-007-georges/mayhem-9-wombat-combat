"""Attack-helicopter module for aerial stunt manoeuvres."""

from __future__ import annotations

from src.weather_api import get_live_wind_speed


class AttackHelicopter:
    """An attack helicopter used for low-altitude stunt sequences."""

    def __init__(self, name: str) -> None:
        """Create an AttackHelicopter.

        Args:
            name: Human-readable identifier (e.g. "Apache-1").
        """
        self.name = name

    def calculate_rotor_pitch(self) -> float:
        """Compute the rotor pitch angle based on live wind speed.

        The pitch is calculated using the formula::

            pitch = base_angle + (wind_speed * adjustment_factor)

        where ``base_angle`` is ``8.0`` degrees and
        ``adjustment_factor`` is ``0.15``.

        Returns:
            Rotor pitch in degrees.

        Raises:
            ConnectionError: The weather service is unavailable.
        """
        base_angle: float = 8.0
        adjustment_factor: float = 0.15
        wind_speed: float = get_live_wind_speed()
        return base_angle + (wind_speed * adjustment_factor)
