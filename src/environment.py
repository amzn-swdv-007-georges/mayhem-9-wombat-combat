"""Environmental conditions affecting vehicle launch safety."""

from __future__ import annotations


class TrackEnvironment:
    """Represents the current track surface conditions.

    Behaves as shared global state.  All vehicle modules read
    ``friction_coefficient`` directly from this class.
    """

    friction_coefficient: float = 0.85
    _oil_slick_applied: bool = False

    @classmethod
    def reset(cls) -> None:
        """Restore the track to its default dry condition."""
        cls.friction_coefficient = 0.85
        cls._oil_slick_applied = False

    @classmethod
    def set_oil_slick(cls) -> None:
        """Apply an oil slick to the track, reducing grip."""
        cls.friction_coefficient = 0.12
        cls._oil_slick_applied = True

    @classmethod
    def is_safe_for_launch(cls) -> bool:
        """Return True if the surface provides sufficient grip for a launch."""
        return cls.friction_coefficient >= 0.50
