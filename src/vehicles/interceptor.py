"""Pursuit interceptor module wrapping the legacy ECU driver."""

from __future__ import annotations

from src.legacy import LegacyECUDriver


class Interceptor:
    """A high-speed pursuit vehicle for chase sequences.

    Wraps the vendor-supplied :class:`LegacyECUDriver` to implement
    a controlled shutdown procedure.
    """

    def __init__(self, name: str) -> None:
        """Create an Interceptor.

        Args:
            name: Human-readable identifier (e.g. "Pursuit-1").
        """
        self.name = name

    def engage_pursuit_mode(self) -> bool:
        """Activate the supercharger for high-speed pursuit.

        Returns:
            True if the supercharger was successfully engaged.
        """
        return LegacyECUDriver.supercharger_engage()

    def shutdown(self) -> bool:
        """Perform a controlled shutdown sequence.

        Cuts ignition via the legacy ECU driver.

        Returns:
            True if the engine was running before shutdown.
        """
        return LegacyECUDriver.ignition_cutoff()
