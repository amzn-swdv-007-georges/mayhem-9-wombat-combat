"""Activity: Mocking vendor-supplied legacy code.

A previous developer attempted to test the interceptor by
directly patching the vendor ECU driver instead of wrapping it
with a Spy that records interactions.

Mocking a compiled binary is fragile — if the vendor updates the
firmware interface the mocks silently drift out of sync with
real behaviour.

Safety regulations require that ``ignition_cutoff`` fires
**before** ``supercharger_engage`` during a shutdown sequence.
If the ECU fires these out of order, the real supercharger
blows through the hood.  The current tests cannot verify this.
"""

from unittest.mock import patch

from src.vehicles.interceptor import Interceptor


def test_interceptor_cuts_ignition_on_shutdown() -> None:
    """The interceptor should command the ECU to cut ignition."""
    with patch("src.vehicles.interceptor.LegacyECUDriver") as mock_ecu:
        mock_ecu.ignition_cutoff.return_value = True
        interceptor = Interceptor("Night Hawk")
        result = interceptor.shutdown()
        mock_ecu.ignition_cutoff.assert_called_once()
        assert result is True


def test_interceptor_engages_supercharger_for_pursuit() -> None:
    """The interceptor should engage the supercharger via the ECU."""
    with patch("src.vehicles.interceptor.LegacyECUDriver") as mock_ecu:
        mock_ecu.supercharger_engage.return_value = True
        interceptor = Interceptor("Night Hawk")
        result = interceptor.engage_pursuit_mode()
        mock_ecu.supercharger_engage.assert_called_once()
        assert result is True


def test_shutdown_sequence_fires_both_ecu_methods() -> None:
    """Both ECU methods must be triggered during the full sequence.

    Note: this test verifies that both methods are called, but it
    cannot check the **order** in which they fire.  The mock can
    count calls but has no way to record their chronology.
    """
    with patch("src.vehicles.interceptor.LegacyECUDriver") as mock_ecu:
        mock_ecu.ignition_cutoff.return_value = True
        mock_ecu.supercharger_engage.return_value = True
        interceptor = Interceptor("Night Hawk")
        interceptor.shutdown()
        interceptor.engage_pursuit_mode()
        mock_ecu.ignition_cutoff.assert_called_once()
        mock_ecu.supercharger_engage.assert_called_once()
        assert mock_ecu.ignition_cutoff.called
        assert mock_ecu.supercharger_engage.called
