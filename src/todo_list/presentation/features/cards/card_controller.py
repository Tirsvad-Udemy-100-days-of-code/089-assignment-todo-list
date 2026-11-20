"""@brief The controller of the card API."""

from todo_list import constants
from todo_list.application.use_cases.card_use_cases import (
    UNSET,
    AddComment,
    CreateCard,
    DeleteCard,
    DeleteComment,
    GetCard,
    MoveCard,
    UpdateCardDetails,
)
from todo_list.presentation.shared.http_request import (
    BadRequestError,
    HttpRequest,
    optional_bool,
    optional_nullable_str,
    optional_str,
    require_int,
    require_str,
)
from todo_list.presentation.shared.http_response import HttpResponse
from todo_list.presentation.shared.json_responses import json_response, no_content


class CardController:
    """@brief Answers the requests that change cards."""

    def __init__(
        self,
        create: CreateCard,
        update: UpdateCardDetails,
        delete: DeleteCard,
        move: MoveCard,
        get: GetCard,
        add_comment: AddComment,
        delete_comment: DeleteComment,
    ) -> None:
        """@param create The use cases the controller calls, in this order."""
        self._create = create
        self._update = update
        self._delete = delete
        self._move = move
        self._get = get
        self._add_comment = add_comment
        self._delete_comment = delete_comment

    def create_card(self, request: HttpRequest) -> HttpResponse:
        """@brief POST /api/lists/{id}/cards with title."""
        data = request.json_object()
        created = self._create.execute(request.path_id(), require_str(data, "title"))
        return json_response(constants.STATUS_CREATED, created)

    def update_card(self, request: HttpRequest) -> HttpResponse:
        """@brief PATCH /api/cards/{id} with any of title, label, description,
        due_date and done; fields that are absent stay unchanged.
        """
        data = request.json_object()
        known = (
            constants.FIELD_TITLE,
            constants.FIELD_LABEL,
            constants.FIELD_DESCRIPTION,
            constants.FIELD_DUE_DATE,
            constants.FIELD_DONE,
        )
        if not any(field in data for field in known):
            raise BadRequestError(constants.ERROR_NO_CHANGES)
        updated = self._update.execute(
            request.path_id(),
            title=optional_str(data, constants.FIELD_TITLE),
            label=optional_str(data, constants.FIELD_LABEL),
            description=optional_str(data, constants.FIELD_DESCRIPTION),
            due_date=optional_nullable_str(data, constants.FIELD_DUE_DATE, UNSET),
            done=optional_bool(data, constants.FIELD_DONE),
        )
        return json_response(constants.STATUS_OK, updated)

    def get_card(self, request: HttpRequest) -> HttpResponse:
        """@brief GET /api/cards/{id}: the card with its comments."""
        return json_response(constants.STATUS_OK, self._get.execute(request.path_id()))

    def add_comment(self, request: HttpRequest) -> HttpResponse:
        """@brief POST /api/cards/{id}/comments with text."""
        data = request.json_object()
        comment = self._add_comment.execute(
            request.path_id(), require_str(data, constants.FIELD_TEXT)
        )
        return json_response(constants.STATUS_CREATED, comment)

    def delete_comment(self, request: HttpRequest) -> HttpResponse:
        """@brief DELETE /api/comments/{id}."""
        self._delete_comment.execute(request.path_id())
        return no_content()

    def move_card(self, request: HttpRequest) -> HttpResponse:
        """@brief PATCH /api/cards/{id}/move with list_id and position."""
        data = request.json_object()
        moved = self._move.execute(
            request.path_id(),
            require_int(data, constants.FIELD_LIST_ID),
            require_int(data, constants.FIELD_POSITION),
        )
        return json_response(constants.STATUS_OK, moved)

    def delete_card(self, request: HttpRequest) -> HttpResponse:
        """@brief DELETE /api/cards/{id}."""
        self._delete.execute(request.path_id())
        return no_content()
