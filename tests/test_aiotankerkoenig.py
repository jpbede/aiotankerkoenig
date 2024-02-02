"""Test the tankerkoenig API client."""
import asyncio
from typing import Any

import aiohttp
from aioresponses import CallbackResult, aioresponses
import pytest
from syrupy import SnapshotAssertion

from aiotankerkoenig import (
    GasType,
    Sort,
    Tankerkoenig,
    TankerkoenigConnectionError,
    TankerkoenigConnectionTimeoutError,
    TankerkoenigError,
    TankerkoenigInvalidKeyError,
)
from tests import load_fixture

TANKERKOENIG_ENDPOINT = "https://creativecommons.tankerkoenig.de"


async def test_timeout(
    responses: aioresponses,
) -> None:
    """Test request timeout."""

    async def response_handler(_: str, **_kwargs: Any) -> CallbackResult:
        """Response handler for this test."""
        await asyncio.sleep(2)
        return CallbackResult(body="Good morning!")

    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        callback=response_handler,
    )
    async with Tankerkoenig(
        api_key="abc123",
        request_timeout=1,
    ) as tankerkoenig_client:
        with pytest.raises(TankerkoenigConnectionTimeoutError):
            await tankerkoenig_client.station_details(station_id="1")


async def test_unexpected_server_response(
    responses: aioresponses,
    tankerkoenig_client: Tankerkoenig,
) -> None:
    """Test handling unexpected response."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        status=200,
        headers={"Content-Type": "plain/text"},
        body="Yes",
    )
    with pytest.raises(TankerkoenigError):
        await tankerkoenig_client.station_details(station_id="1")


async def test_non_200_response(
    responses: aioresponses,
    tankerkoenig_client: Tankerkoenig,
) -> None:
    """Test handling unexpected response."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        status=500,
        headers={"Content-Type": "plain/text"},
        body="Yes",
    )
    with pytest.raises(TankerkoenigConnectionError):
        await tankerkoenig_client.station_details(station_id="1")


@pytest.mark.parametrize(
    "message",
    [
        "API-Key existiert nicht",
        "APIKey existiert nicht.",
    ],
)
async def test_invalid_apikey_response(
    responses: aioresponses,
    tankerkoenig_client: Tankerkoenig,
    message: str,
) -> None:
    """Test handling of invalid api key response."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        status=200,
        body='{"status": "error", "ok": false, "message": "' + message + '"}',
    )
    with pytest.raises(TankerkoenigInvalidKeyError):
        await tankerkoenig_client.station_details(station_id="1")


async def test_general_error_response(
    responses: aioresponses,
    tankerkoenig_client: Tankerkoenig,
) -> None:
    """Test handling of a general error response."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        status=200,
        body='{"status": "error", "ok": false, "message": "Idk what happened!"}',
    )
    with pytest.raises(TankerkoenigError):
        await tankerkoenig_client.station_details(station_id="1")


async def test_putting_in_own_session(
    responses: aioresponses,
) -> None:
    """Test putting in own session."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        status=200,
        body=load_fixture("detail.json"),
    )
    async with aiohttp.ClientSession() as session:
        tankerkoenig = Tankerkoenig(api_key="abc123", session=session)
        await tankerkoenig.station_details(station_id="1")
        assert tankerkoenig.session is not None
        assert not tankerkoenig.session.closed
        await tankerkoenig.close()
        assert not tankerkoenig.session.closed


async def test_creating_own_session(
    responses: aioresponses,
) -> None:
    """Test creating own session."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        status=200,
        body=load_fixture("detail.json"),
    )
    tankerkoenig = Tankerkoenig(api_key="abc123")
    await tankerkoenig.station_details(station_id="1")
    assert tankerkoenig.session is not None
    assert not tankerkoenig.session.closed
    await tankerkoenig.close()
    assert tankerkoenig.session.closed


async def test_station_details(
    responses: aioresponses,
    tankerkoenig_client: Tankerkoenig,
    snapshot: SnapshotAssertion,
) -> None:
    """Test retrieving station details."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/detail.php?apikey=abc123&id=1",
        status=200,
        body=load_fixture("detail.json"),
    )
    assert await tankerkoenig_client.station_details(station_id="1") == snapshot


async def test_nearby_stations(
    responses: aioresponses,
    tankerkoenig_client: Tankerkoenig,
    snapshot: SnapshotAssertion,
) -> None:
    """Test retrieving nearby stations."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/list.php?apikey=abc123&lat=53.1&lng=7.8&rad=5&sort=dist&type=all",
        status=200,
        body=load_fixture("list.json"),
    )
    assert (
        await tankerkoenig_client.nearby_stations(
            coordinates=(53.1, 7.8),
            radius=5,
            gas_type=GasType.ALL,
            sort=Sort.DISTANCE,
        )
        == snapshot
    )


async def test_prices(
    responses: aioresponses,
    tankerkoenig_client: Tankerkoenig,
    snapshot: SnapshotAssertion,
) -> None:
    """Test retrieving nearby stations."""
    responses.get(
        f"{TANKERKOENIG_ENDPOINT}/json/prices.php?apikey=abc123&ids=4fd02fd5-0a4c-46b3-a9b9-a488a62454be",
        status=200,
        body=load_fixture("prices.json"),
    )
    assert (
        await tankerkoenig_client.prices(
            station_ids=["4fd02fd5-0a4c-46b3-a9b9-a488a62454be"],
        )
        == snapshot
    )
