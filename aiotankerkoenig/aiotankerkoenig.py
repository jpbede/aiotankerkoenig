"""Tankerkoenig API client."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from importlib import metadata
from typing import Any, Self

from aiohttp import ClientSession
from yarl import URL

from .const import GasType, Sort
from .exceptions import TankerkoenigConnectionError, TankerkoenigError
from .models import (
    PriceInfo,
    PriceInfoResponse,
    Station,
    StationDetailResponse,
    StationListResponse,
)

VERSION = metadata.version(__package__)


@dataclass
class Tankerkoenig:
    """Tankerkoenig API client."""

    api_key: str
    session: ClientSession | None = None
    request_timeout: int = 10

    _close_session: bool = False

    async def _request(self, path: str, params: dict[str, Any]) -> str:
        """Handle request to tankerkoenig.de API."""
        url = URL.build(
            scheme="https",
            host="creativecommons.tankerkoenig.de",
            path=path,
            query={"apikey": self.api_key, **params},
        )

        headers = {
            "Accept": "application/json",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True
            headers.update(
                {
                    "User-Agent": f"aiotankerkoenig/{VERSION}",
                },
            )

        try:
            async with asyncio.timeout(self.request_timeout):
                response = await self.session.get(
                    url,
                    headers=headers,
                )
        except asyncio.TimeoutError as exception:
            msg = "Timeout occurred while connecting to tankerkoenig.de API"
            raise TankerkoenigConnectionError(
                msg,
            ) from exception

        content_type = response.headers.get("Content-Type", "")
        text = await response.text()
        if "application/json" not in content_type:
            msg = "Unexpected content type from tankerkoenig.de API"
            raise TankerkoenigError(
                msg,
                {"Content-Type": content_type, "response": text},
            )

        return text

    async def nearby_stations(
        self,
        coordinates: tuple[float, float],
        radius: int,
        gas_type: GasType,
        sort: Sort,
    ) -> list[Station]:
        """Get nearby stations."""
        result = await self._request(
            path="/json/list.php",
            params={
                "lat": coordinates[0],
                "lng": coordinates[1],
                "rad": radius,
                "type": gas_type,
                "sort": sort,
            },
        )
        return StationListResponse.from_json(result).stations

    async def station_details(
        self,
        station_id: str,
    ) -> Station:
        """Get station details."""
        result = await self._request(
            path="/json/detail.php",
            params={
                "id": station_id,
            },
        )
        return StationDetailResponse.from_json(result).station

    async def prices(
        self,
        station_ids: list[str],
    ) -> dict[str, PriceInfo]:
        """Get station details."""
        result = await self._request(
            path="/json/prices.php",
            params={
                "ids": ",".join(station_ids),
            },
        )
        return PriceInfoResponse.from_json(result).prices

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> Self:
        """Async enter."""
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.    _exc_info: Exec type."""
        await self.close()
