"""Tankerkoenig API client."""
from __future__ import annotations

from .aiotankerkoenig import Tankerkoenig
from .const import GasType, Sort, Status
from .exceptions import (
    TankerkoenigConnectionError,
    TankerkoenigError,
    TankerkoenigInvalidKeyError,
)
from .models import PriceInfo, Station

__all__ = [
    "Tankerkoenig",
    "TankerkoenigError",
    "TankerkoenigConnectionError",
    "TankerkoenigInvalidKeyError",
    "GasType",
    "Sort",
    "Status",
    "PriceInfo",
    "Station",
]
