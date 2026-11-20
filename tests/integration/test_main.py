"""Integration test of the composition root."""

import logging
from http.server import ThreadingHTTPServer
from pathlib import Path

import pytest

from todo_list.main import main


def test_main_stops_cleanly_on_keyboard_interrupt(
    monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture, tmp_path: Path
) -> None:
    def interrupt(self: ThreadingHTTPServer, poll_interval: float = 0.5) -> None:
        raise KeyboardInterrupt

    monkeypatch.setattr(ThreadingHTTPServer, "serve_forever", interrupt)

    with caplog.at_level(logging.INFO):
        main("127.0.0.1", 0, tmp_path / "main.sqlite3")

    assert "Stopping" in caplog.text
