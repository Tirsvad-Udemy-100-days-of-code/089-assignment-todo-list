"""@brief The controller of the card API."""

from todo_list import constants
from todo_list.application.use_cases.card_use_cases import (
    CreateCard,
    DeleteCard,
    RenameCard,
)
from todo_list.presentation.shared.http_request import HttpRequest, require_str
from todo_list.presentation.shared.http_response import HttpResponse
from todo_list.presentation.shared.json_responses import json_response, no_content


class CardController:
    """@brief Answers the requests that change cards."""

    def __init__(
        self, create: CreateCard, rename: RenameCard, delete: DeleteCard
    ) -> None:
        """@param create The use cases the controller calls (create, rename, delete)."""
        self._create = create
        self._rename = rename
        self._delete = delete

    def create_card(self, request: HttpRequest) -> HttpResponse:
        """@brief POST /api/lists/{id}/cards with title."""
        data = request.json_object()
        created = self._create.execute(request.path_id(), require_str(data, "title"))
        return json_response(constants.STATUS_CREATED, created)

    def rename_card(self, request: HttpRequest) -> HttpResponse:
        """@brief PATCH /api/cards/{id} with title."""
        data = request.json_object()
        renamed = self._rename.execute(request.path_id(), require_str(data, "title"))
        return json_response(constants.STATUS_OK, renamed)

    def delete_card(self, request: HttpRequest) -> HttpResponse:
        """@brief DELETE /api/cards/{id}."""
        self._delete.execute(request.path_id())
        return no_content()
