"""Activity: Spy pattern for vendor-supplied legacy code.

A Spy wraps the real LegacyECUDriver, delegating every call to the
real implementation while recording what was called and in what
order.  This allows chronological assertions that mocks cannot
provide.
"""

from unittest.mock import call, patch

from src.legacy import LegacyECUDriver
from src.vehicles.interceptor import Interceptor


def test_interceptor_cuts_ignition_on_shutdown() -> None:
    """The interceptor should command the ECU to cut ignition."""
    with patch("src.vehicles.interceptor.LegacyECUDriver", wraps=LegacyECUDriver) as spy:
        interceptor = Interceptor("Night Hawk")
        result = interceptor.shutdown()

    spy.ignition_cutoff.assert_called_once()
    assert result is False


def test_interceptor_engages_supercharger_for_pursuit() -> None:
    """The interceptor should engage the supercharger via the ECU."""
    with patch("src.vehicles.interceptor.LegacyECUDriver", wraps=LegacyECUDriver) as spy:
        interceptor = Interceptor("Night Hawk")
        result = interceptor.engage_pursuit_mode()

    spy.supercharger_engage.assert_called_once()
    assert result is True


def test_shutdown_sequence_fires_both_ecu_methods() -> None:
    """Both ECU methods must be triggered during the full sequence,
    with ignition_cutoff firing chronologically before
    supercharger_engage.
    """
    with patch("src.vehicles.interceptor.LegacyECUDriver", wraps=LegacyECUDriver) as spy:
        interceptor = Interceptor("Night Hawk")
        interceptor.shutdown()
        interceptor.engage_pursuit_mode()

    spy.ignition_cutoff.assert_called_once()
    spy.supercharger_engage.assert_called_once()
    spy.assert_has_calls([call.ignition_cutoff(), call.supercharger_engage()])
