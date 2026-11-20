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

## @brief JSON fields of the move requests.
FIELD_LIST_ID = "list_id"
FIELD_POSITION = "position"

## @brief Largest request body the server reads, in bytes.
MAX_BODY_BYTES = 65536

## @brief The label colours a card may have; an empty label means none.
LABEL_COLOURS = ("red", "orange", "yellow", "green", "blue", "purple")

## @brief Longest card description, in characters.
MAX_DESCRIPTION_LENGTH = 2000

## @brief Longest comment, in characters.
MAX_COMMENT_LENGTH = 500

## @brief Messages shown when a card detail is not valid.
ERROR_LABEL_INVALID = "The label must be empty or one of: " + ", ".join(LABEL_COLOURS)
ERROR_DESCRIPTION_TOO_LONG = "A description must be at most 2000 characters."
ERROR_DUE_DATE_INVALID = "The due date must be a date written as YYYY-MM-DD."
ERROR_COMMENT_EMPTY = "A comment must not be empty."
ERROR_COMMENT_TOO_LONG = "A comment must be at most 500 characters."
ERROR_NO_CHANGES = "The request changes nothing: give at least one field."

## @brief JSON fields of the card detail requests.
FIELD_TITLE = "title"
FIELD_LABEL = "label"
FIELD_DESCRIPTION = "description"
FIELD_DUE_DATE = "due_date"
FIELD_DONE = "done"
FIELD_TEXT = "text"

## @brief Schema version written to PRAGMA user_version once the card details exist.
SCHEMA_VERSION = 1
