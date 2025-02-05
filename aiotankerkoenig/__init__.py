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
    "GasType",
    "PriceInfo",
    "Sort",
    "Station",
    "Status",
    "Tankerkoenig",
    "TankerkoenigConnectionError",
    "TankerkoenigConnectionTimeoutError",
    "TankerkoenigError",
    "TankerkoenigInvalidKeyError",
    "TankerkoenigRateLimitError",
]
