"""Models for the aiotankerkoenig client."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from mashumaro import DataClassDictMixin, field_options


class GasType(StrEnum):
    """Gas type."""

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


@dataclass(frozen=True, slots=True)
class OpeningTime(DataClassDictMixin):
    """Class representing a station opening time."""

    end: str
    start: str
    text: str


@dataclass(frozen=True, slots=True)
class Station(DataClassDictMixin):
    """Class representing a station."""

    id: str
    name: str
    house_number: str = field(metadata=field_options(alias="houseNumber"))
    place: str
    post_code: int = field(metadata=field_options(alias="postCode"))
    street: str
    lat: float
    lng: float

    # only available in detail view
    brand: str | None = None
    diesel: float | None = None
    e10: float | None = None
    e5: float | None = None
    is_open: bool | None = field(metadata=field_options(alias="isOpen"), default=None)
    overrides: Any | None = None
    whole_day: bool | None = field(
        metadata=field_options(alias="wholeDay"),
        default=None,
    )
    state: str | None = None
    opening_times: list[OpeningTime] | None = field(
        metadata=field_options(alias="opening_times"),
        default=None,
    )


@dataclass(frozen=True, slots=True)
class PriceInfo(DataClassDictMixin):
    """Class representing a station price info."""

    status: Status = Status.UNKNOWN
    e5: float | None = None
    e10: float | None = None
    diesel: float | None = None
