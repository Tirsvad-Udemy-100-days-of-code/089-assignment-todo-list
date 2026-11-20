"""@brief The one home of the project's constants.

Every literal that more than one place needs, or that a reader may want to
change, is defined here once.
"""

from http import HTTPStatus

## @brief Title shown in the browser tab and the page header.
APP_TITLE = "Todo List"

## @brief Interface the server listens on; local use only.
DEFAULT_HOST = "127.0.0.1"

## @brief Port the server listens on.
DEFAULT_PORT = 8000

## @brief File name of the SQLite database.
DATABASE_FILE_NAME = "todo_list.sqlite3"

## @brief Names of the lists a new board starts with, in display order.
DEFAULT_LIST_NAMES = ("Backlog", "To Do", "In Progress", "Review", "Done")

## @brief Path of the board page.
ROUTE_HOME = "/"

## @brief Content type of the HTML pages.
CONTENT_TYPE_HTML = "text/html; charset=utf-8"

## @brief Text encoding of every response body.
ENCODING = "utf-8"

## @brief Status code of a successful response.
STATUS_OK = HTTPStatus.OK

## @brief Status code of an unknown path.
STATUS_NOT_FOUND = HTTPStatus.NOT_FOUND

## @brief Name of the board created on first start.
DEFAULT_BOARD_NAME = "My Board"

## @brief Longest name or title, in characters.
MAX_NAME_LENGTH = 100

## @brief Messages shown when a name is not valid.
ERROR_NAME_EMPTY = "A name must not be empty."
ERROR_NAME_TOO_LONG = "A name must be at most 100 characters."

## @brief Content types of the responses.
CONTENT_TYPE_JSON = "application/json; charset=utf-8"
CONTENT_TYPE_JS = "text/javascript; charset=utf-8"
CONTENT_TYPE_CSS = "text/css; charset=utf-8"

## @brief Status codes the API uses besides OK and not found.
STATUS_CREATED = HTTPStatus.CREATED
STATUS_NO_CONTENT = HTTPStatus.NO_CONTENT
STATUS_BAD_REQUEST = HTTPStatus.BAD_REQUEST
STATUS_METHOD_NOT_ALLOWED = HTTPStatus.METHOD_NOT_ALLOWED

## @brief Static files served under /static/, with their content types.
STATIC_ROUTE_PREFIX = "/static/"
STATIC_FILES = {
    "app.js": CONTENT_TYPE_JS,
    "style.css": CONTENT_TYPE_CSS,
}

## @brief Messages of API errors.
ERROR_INVALID_JSON = "The request body must be a JSON object."
ERROR_FIELD_MISSING = "The field is missing or has the wrong type: "
ERROR_NOT_FOUND = "Not found."
ERROR_METHOD_NOT_ALLOWED = "Method not allowed."

## @brief Largest request body the server reads, in bytes.
MAX_BODY_BYTES = 65536
