"""@brief The controller of the list API."""

from todo_list import constants
from todo_list.application.use_cases.list_use_cases import (
    CreateList,
    DeleteList,
    RenameList,
)
from todo_list.presentation.shared.http_request import (
    HttpRequest,
    require_int,
    require_str,
)
from todo_list.presentation.shared.http_response import HttpResponse
from todo_list.presentation.shared.json_responses import json_response, no_content


class ListController:
    """@brief Answers the requests that change lists."""

    def __init__(
        self, create: CreateList, rename: RenameList, delete: DeleteList
    ) -> None:
        """@param create The use cases the controller calls (create, rename, delete)."""
        self._create = create
        self._rename = rename
        self._delete = delete

    def create_list(self, request: HttpRequest) -> HttpResponse:
        """@brief POST /api/lists with board_id and name."""
        data = request.json_object()
        created = self._create.execute(
            require_int(data, "board_id"), require_str(data, "name")
        )
        return json_response(constants.STATUS_CREATED, created)

    def rename_list(self, request: HttpRequest) -> HttpResponse:
        """@brief PATCH /api/lists/{id} with name."""
        data = request.json_object()
        renamed = self._rename.execute(request.path_id(), require_str(data, "name"))
        return json_response(constants.STATUS_OK, renamed)

    def delete_list(self, request: HttpRequest) -> HttpResponse:
        """@brief DELETE /api/lists/{id}."""
        self._delete.execute(request.path_id())
        return no_content()
