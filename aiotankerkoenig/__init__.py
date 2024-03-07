"""Tankerkoenig API client."""

from __future__ import annotations

from .aiotankerkoenig import Tankerkoenig
from .const import GasType, Sort, Status
from .exceptions import (
    TankerkoenigConnectionError,
    TankerkoenigConnectionTimeoutError,
    TankerkoenigError,
    TankerkoenigInvalidKeyError,
    TankerkoenigRateLimitError,
)
from .models import PriceInfo, Station

__all__ = [
    "Tankerkoenig",
    "TankerkoenigError",
    "TankerkoenigConnectionError",
    "TankerkoenigInvalidKeyError",
    "TankerkoenigConnectionTimeoutError",
    "TankerkoenigRateLimitError",
    "GasType",
    "Sort",
    "Status",
    "PriceInfo",
    "Station",
]
