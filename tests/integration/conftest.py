"""Fixtures shared by the integration tests."""

from collections.abc import Iterator
from pathlib import Path

import pytest

from support.api_client import ApiClient
from support.running_server import running_server


@pytest.fixture
def base_url(tmp_path: Path) -> Iterator[str]:
    """A running server on a free port with its own database file."""
    with running_server(tmp_path / "server.sqlite3") as url:
        yield url


@pytest.fixture
def api(base_url: str) -> ApiClient:
    """A client of the running server."""
    return ApiClient(base_url)
