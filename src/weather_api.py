"""External weather service client.

Connects to the Australian Bureau of Meteorology (bom.gov.au) for
real-time wind speed readings.
"""

from __future__ import annotations


def get_live_wind_speed() -> float:
    """Query the live wind speed in metres per second from bom.gov.au.

    Returns:
        Current wind speed in m/s.

    Raises:
        ConnectionError: The external weather service is currently
            unreachable.
    """
    raise ConnectionError("Unable to reach bom.gov.au — network unavailable")
