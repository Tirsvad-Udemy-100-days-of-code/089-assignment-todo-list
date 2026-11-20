"""@brief Runs the application server on a free port for the length of a block."""

import threading
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from todo_list.main import build_router_for
from todo_list.presentation.http_server import create_server


@contextmanager
def running_server(database_path: Path) -> Iterator[str]:
    """@brief Start the server on a free port and stop it afterwards.

    @param database_path The SQLite file the server uses.
    @return The base URL, for example http://127.0.0.1:54321.
    """
    server = create_server("127.0.0.1", 0, build_router_for(database_path))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    host, port = server.server_address[:2]
    try:
        yield f"http://{host!s}:{port}"
    finally:
        server.shutdown()
        server.server_close()
