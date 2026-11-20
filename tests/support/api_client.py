"""@brief A tiny HTTP client for the integration tests, standard library only."""

import json
import urllib.error
import urllib.request
from typing import Any


class ApiClient:
    """@brief Sends requests to a running server and returns status and JSON."""

    def __init__(self, base_url: str) -> None:
        """@param base_url The server address, for example http://127.0.0.1:8000."""
        self._base_url = base_url

    def request(self, method: str, path: str, body: object = None) -> tuple[int, Any]:
        """@brief Send one request.

        @return The status code and the parsed JSON (None for an empty body).
        """
        data = None if body is None else json.dumps(body).encode()
        request = urllib.request.Request(
            self._base_url + path,
            data=data,
            method=method,
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(request) as response:
                status, raw = response.status, response.read()
        except urllib.error.HTTPError as error:
            status, raw = error.code, error.read()
        return status, (json.loads(raw) if raw else None)

    def request_raw(self, method: str, path: str, raw: bytes) -> tuple[int, str]:
        """@brief Send a raw body; return the status and the body text."""
        request = urllib.request.Request(self._base_url + path, data=raw, method=method)
        try:
            with urllib.request.urlopen(request) as response:
                return response.status, response.read().decode()
        except urllib.error.HTTPError as error:
            return error.code, error.read().decode()
