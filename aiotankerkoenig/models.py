"""Models for the aiotankerkoenig client."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Self

from mashumaro import field_options
from mashumaro.mixins.orjson import DataClassORJSONMixin

from .const import Status
from .exceptions import TankerkoenigError, TankerkoenigInvalidKeyError


@dataclass(frozen=True, slots=True, kw_only=True)
class TankerkoenigResponse(DataClassORJSONMixin):
    """Base class for all responses."""

    @classmethod
    def __pre_deserialize__(
        cls: type[Self],
        d: dict[Any, Any],
    ) -> dict[Any, Any]:
        """Raise when response was unexpected."""
        if d.get("ok"):
            return d

        message = d.get("message", "")
        if any(x in message.lower() for x in ("api-key", "apikey")):
            msg = "tankerkoenig.de API responded with an invalid key error"
            raise TankerkoenigInvalidKeyError(
                msg,
                {"response": d},
            )

        msg = f"tankerkoenig.de API responded with an error: {message}"
        raise TankerkoenigError(
            msg,
            {"response": d.pop("message")},
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class StationListResponse(TankerkoenigResponse):
    """Class representing a station list response."""

    stations: list[Station]


@dataclass(frozen=True, slots=True, kw_only=True)
class StationDetailResponse(TankerkoenigResponse):
    """Class representing a station response."""

    station: Station


@dataclass(frozen=True, slots=True, kw_only=True)
class PriceInfoResponse(TankerkoenigResponse):
    """Class representing a station price info response."""

    prices: dict[str, PriceInfo]


@dataclass(frozen=True, slots=True, kw_only=True)
class OpeningTime:
    """Class representing a station opening time."""

    end: str
    start: str
    text: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Station:
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
    distance: float | None = field(metadata=field_options(alias="dist"), default=None)


@dataclass(frozen=True, slots=True, kw_only=True)
class PriceInfo:
    """Class representing a station price info."""

    status: Status = Status.UNKNOWN
    e5: float | None = None
    e10: float | None = None
    diesel: float | None = None
