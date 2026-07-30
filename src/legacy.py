"""Vendor-supplied ECU driver — DO NOT MODIFY.

This module provides a Python interface to a compiled binary Engine
Control Unit driver supplied by the manufacturer.  It is treated as
a black box and must not be changed.  Tests that depend on this
driver should use stubbing or mocking rather than altering the
implementation.
"""

from __future__ import annotations


class LegacyECUDriver:
    """Binary-shim for the vendor-supplied ECU firmware."""

    _engine_running: bool = False
    _supercharger_active: bool = False

    @classmethod
    def ignition_cutoff(cls) -> bool:
        """Cut power to the ignition system.

        Returns:
            True if the engine was running and has now stopped.
        """
        was_running = cls._engine_running
        cls._engine_running = False
        cls._supercharger_active = False
        return was_running

    @classmethod
    def supercharger_engage(cls) -> bool:
        """Engage the supercharger if the engine is running.

        Returns:
            True if the supercharger was successfully engaged.
        """
        if not cls._engine_running:
            cls._engine_running = True
        cls._supercharger_active = True
        return True

    @classmethod
    def is_engine_running(cls) -> bool:
        """Return True if the engine is currently running."""
        return cls._engine_running

    @classmethod
    def is_supercharger_active(cls) -> bool:
        """Return True if the supercharger is currently engaged."""
        return cls._supercharger_active
