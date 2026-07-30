"""Financial operations for stunt insurance and equipment telemetry."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Transfer:
    """Record of a single insurance fund transfer."""

    amount: float
    recipient: str
    reference: str


_transfer_ledger: list[Transfer] = []


def wire_insurance_funds(amount: float, recipient: str, reference: str) -> Transfer:
    """Transfer insurance funds to a production unit.

    Args:
        amount: Dollar amount to transfer.
        recipient: Name of the receiving production unit.
        reference: Invoice or purchase-order reference string.

    Returns:
        The recorded Transfer.
    """
    transfer = Transfer(amount=amount, recipient=recipient, reference=reference)
    _transfer_ledger.append(transfer)
    return transfer


def list_transfers() -> list[Transfer]:
    """Return all recorded insurance transfers."""
    return list(_transfer_ledger)


def process_canyon_chase_insurance() -> None:
    """Wire the insurance payment for the jet-mower canyon chase sequence.

    Covers engine-meltdown liability for two jet-powered ride-on
    lawnmowers racing through a narrow outback canyon at 140 km/h.
    """
    wire_insurance_funds(100_000, "Canyon Chase Unit A", "CANYON-042")
    wire_insurance_funds(100_000, "Canyon Chase Unit A", "CANYON-042")


def get_engine_temperature() -> float:
    """Return a simulated engine temperature reading in degrees Celsius."""
    return 92.3
