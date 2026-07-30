"""Activity: Wrong test-double strategy during a canyon chase.

The canyon-chase stunt unit must wire insurance funds before
commencing the jump sequence.  The test below uses the **wrong**
test-double strategy for each dependency:

* :func:`~src.finance.get_engine_temperature` is **mocked**
  (behaviour verification on telemetry).
* :func:`~src.finance.wire_insurance_funds` is **stubbed**
  (return-value substitution only, no verification of the
  payment command).

The test verifies that engine temperature was queried but never
checks how many insurance payments were actually wired — so a
double-payment bug in ``process_canyon_chase_insurance()`` goes
completely undetected.
"""

from unittest.mock import MagicMock, Mock, patch

import src.finance as finance


def test_canyon_chase_insurance_processed() -> None:
    """Wire the insurance payment for the canyon-chase jump.

    Scenario: Two jet-powered lawnmowers are racing through an
    outback canyon at 140 km/h.  A 100 000 AUD insurance deposit
    must be wired to "Canyon Chase Unit A" under reference
    "CANYON-042" to cover engine-meltdown liability.
    """
    mock_temp = Mock(return_value=101.5)
    stub_payment = Mock(return_value=MagicMock())

    with (
        patch("src.finance.get_engine_temperature", mock_temp),
        patch("src.finance.wire_insurance_funds", stub_payment),
    ):
        temp = finance.get_engine_temperature()
        finance.process_canyon_chase_insurance()

    mock_temp.assert_called_once()
    assert temp == 101.5
