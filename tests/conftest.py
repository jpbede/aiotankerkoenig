"""Fixtures for aioelectricitymaps tests."""

from collections.abc import AsyncGenerator

import aiohttp
from aiointercept import aiointercept
import pytest

from aiotankerkoenig import Tankerkoenig


@pytest.fixture(name="tankerkoenig_client")
async def client() -> AsyncGenerator[Tankerkoenig, None]:
    """Return a Spotify client."""
    async with (
        aiohttp.ClientSession() as session,
        Tankerkoenig(
            session=session,
            api_key="abc123",
        ) as tankerkoenig_client,
    ):
        yield tankerkoenig_client


@pytest.fixture(name="responses")
async def aiointercept_fixture() -> AsyncGenerator[aiointercept, None]:
    """Return aiointercept fixture."""
    async with aiointercept(mock_external_urls=True) as mocked_responses:
        yield mocked_responses
