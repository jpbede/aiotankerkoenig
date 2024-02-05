"""Fixtures for aioelectricitymaps tests."""
from collections.abc import AsyncGenerator, Generator

import aiohttp
from aioresponses import aioresponses
import pytest

from aiotankerkoenig import Tankerkoenig


@pytest.fixture(name="tankerkoenig_client")
async def client() -> AsyncGenerator[Tankerkoenig, None]:
    """Return a Spotify client."""
    async with aiohttp.ClientSession() as session, Tankerkoenig(
        session=session,
        api_key="abc123",
    ) as tankerkoenig_client:
        yield tankerkoenig_client


@pytest.fixture(name="responses")
def aioresponses_fixture() -> Generator[aioresponses, None, None]:
    """Return aioresponses fixture."""
    with aioresponses() as mocked_responses:
        yield mocked_responses
