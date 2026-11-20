**English** · [Dansk](Step-4-Kanban-Board-da) · [Bahasa Malaysia](Step-4-Kanban-Board-ms)

# Step 4: Kanban board and drag and drop

![Step 4: a card dragged from To Do to Review](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-04.png)

## What we built

The board now behaves like a Kanban board. Cards move between lists and within a list, and lists move left and right, all by drag and drop. Every move is saved: after a reload the board looks the same.

The wireframe that guided the look (blue background, rounded list columns, white cards, an Add a card control under each list):

![Wireframe of the board](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/wireframes/board.svg)

## What we gained

- **Two move endpoints.** `PATCH /api/cards/{id}/move` takes `list_id` and `position`; `PATCH /api/lists/{id}/move` takes `position`. The store renumbers the neighbours in one transaction, so positions never have gaps and a position past the end means the end.
- **Native drag and drop.** The browser's `dragstart`, `dragover` and `drop` events are enough. The drop position is the number of cards whose middle is above the pointer.
- **Visual feedback.** A dragged card fades, and the list under the pointer gets a dashed outline.
- **A responsive layout.** The board scrolls sideways on narrow screens, and lists never get wider than the screen.
- **Browser tests for drag.** Tests in a Docker container drag a card and a list and check the order after a reload.
