"""Constants for the aiotankerkoenig."""
from enum import StrEnum


class GasType(StrEnum):
    """Gas type."""

    ALL = "all"
    DIESEL = "diesel"
    E5 = "e5"
    E10 = "e10"


class Sort(StrEnum):
    """Sort type."""

    DISTANCE = "dist"
    PRICE = "price"
    TIME = "time"


class Status(StrEnum):
    """Status type."""

    OPEN = "open"
    CLOSED = "closed"
    UNKNOWN = "unknown"
