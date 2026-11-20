**English** · [Dansk](Step-3-Api-Editing-da) · [Bahasa Malaysia](Step-3-Api-Editing-ms)

# Step 3: JSON API and editing

![Step 3: a new list and a card form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-03.png)

## What we built

A JSON API for lists and cards and a page that uses it: you can add, rename and delete lists and cards without reloading the page. The server only sends a small HTML shell; plain JavaScript builds the board.

## The API

| Method and path | What it does | Success |
| --- | --- | --- |
| `GET /api/board` | The board with its lists and cards | 200 |
| `POST /api/lists` | Add a list (`board_id`, `name`) | 201 |
| `PATCH /api/lists/{id}` | Rename a list | 200 |
| `DELETE /api/lists/{id}` | Delete a list and its cards | 204 |
| `POST /api/lists/{id}/cards` | Add a card (`title`) | 201 |
| `PATCH /api/cards/{id}` | Rename a card | 200 |
| `DELETE /api/cards/{id}` | Delete a card | 204 |

Errors are JSON with an `error` message: 400 for a bad name or body, 404 for an unknown id or path, 405 for a wrong method. A stack trace is never sent.

## What we gained

- **A small router.** Routes map a method and a path pattern (`{id}`) to a controller function; one place turns domain errors into status codes.
- **HTTP in plain Python.** `http.server` reads the body and writes the response; the controllers never see sockets.
- **Validation at the edge.** `require_str` and `require_int` check each JSON field before a use case runs.
- **A page without a framework.** `app.js` uses `fetch`, builds the DOM with `textContent` (so names cannot inject HTML) and redraws after each change.
- **Browser tests without the desktop.** The end-to-end tests run in a Docker container with a headless browser and write their result to a file.
