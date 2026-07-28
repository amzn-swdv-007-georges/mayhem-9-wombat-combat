"""Monster-truck vehicle module for stunt ramp launches."""

from __future__ import annotations

from src.environment import TrackEnvironment


class MonsterTruck:
    """A monster truck used for ramp-to-ramp stunt jumps."""

    def __init__(self, name: str) -> None:
        """Create a MonsterTruck.

        Args:
            name: Human-readable identifier (e.g. "Grave Digger").
        """
        self.name = name

    def can_launch(self) -> bool:
        """Check whether the track surface provides enough grip to launch.

        Returns:
            True if the current friction coefficient meets the
            minimum threshold for a safe launch.
        """
        return TrackEnvironment.is_safe_for_launch()

    def perform_launch(self) -> str:
        """Execute a ramp launch.

        Returns:
            ``"LAUNCHED"`` on success, ``"ABORTED"`` when the track
            is too slippery.
        """
        if not self.can_launch():
            return "ABORTED"
        return "LAUNCHED"
