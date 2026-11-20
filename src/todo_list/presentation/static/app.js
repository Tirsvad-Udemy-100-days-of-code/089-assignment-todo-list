"use strict";

/** Plain JavaScript client of the board API; builds the DOM with textContent only. */

const state = { board: null };

async function request(method, url, body) {
  const options = { method, headers: { "Content-Type": "application/json" } };
  if (body !== undefined) {
    options.body = JSON.stringify(body);
  }
  const response = await fetch(url, options);
  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(data.error || response.statusText);
  }
  return response.status === 204 ? null : response.json();
}

function element(tag, className, text) {
  const node = document.createElement(tag);
  if (className) {
    node.className = className;
  }
  if (text !== undefined) {
    node.textContent = text;
  }
  return node;
}

function iconButton(label, symbol, onClick) {
  const button = element("button", "icon-button", symbol);
  button.type = "button";
  button.setAttribute("aria-label", label);
  button.addEventListener("click", onClick);
  return button;
}

function showError(message) {
  document.getElementById("error").textContent = message;
}

async function act(action) {
  try {
    showError("");
    await action();
    state.board = await request("GET", "/api/board");
    render();
  } catch (error) {
    showError(error.message);
  }
}

/** Replace `node` with a one-line form; `onSubmit(value)` runs on Enter or the button. */
function inlineForm(node, initial, buttonText, onSubmit, label) {
  const form = element("form", "inline-form");
  const input = element("input");
  input.value = initial;
  input.setAttribute("aria-label", label);
  const submit = element("button", "", buttonText);
  submit.type = "submit";
  form.append(input, submit);
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    onSubmit(input.value);
  });
  input.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      render();
    }
  });
  node.replaceWith(form);
  input.focus();
  input.select();
}

const LABELS = ["red", "orange", "yellow", "green", "blue", "purple"];

/** True when the due date is before today and the card is not done. */
function isOverdue(card) {
  if (!card.due_date || card.done) {
    return false;
  }
  const now = new Date();
  const today = [
    now.getFullYear(),
    String(now.getMonth() + 1).padStart(2, "0"),
    String(now.getDate()).padStart(2, "0"),
  ].join("-");
  return card.due_date < today;
}

function renderBadges(card) {
  const badges = element("div", "badges");
  if (card.due_date) {
    badges.append(element("span", "badge due", `\u{1F4C5} ${card.due_date}`));
  }
  if (card.description) {
    const icon = element("span", "badge description", "≡");
    icon.title = "Has a description";
    badges.append(icon);
  }
  if (card.comment_count > 0) {
    badges.append(element("span", "badge comments", `\u{1F4AC} ${card.comment_count}`));
  }
  return badges;
}

function renderCard(card) {
  const node = element("div", "card");
  node.draggable = true;
  node.dataset.cardId = String(card.id);
  node.classList.toggle("done", card.done);
  node.classList.toggle("overdue", isOverdue(card));
  node.addEventListener("dragstart", (event) => startDrag(event, "card", card.id, node));
  node.addEventListener("dragend", endDrag);
  node.addEventListener("click", (event) => {
    if (event.target.closest(".card-body")) {
      openDetails(card.id);
    }
  });
  const body = element("div", "card-body");
  if (card.label) {
    body.append(element("div", `label-bar label-${card.label}`));
  }
  const title = element("span", "card-title", card.title);
  body.append(title, renderBadges(card));
  node.append(
    body,
    iconButton(`Rename card ${card.title}`, "✎", () =>
      inlineForm(title, card.title, "Save", (value) =>
        act(() => request("PATCH", `/api/cards/${card.id}`, { title: value })), "Card title")),
    iconButton(`Delete card ${card.title}`, "✕", () =>
      act(() => request("DELETE", `/api/cards/${card.id}`))),
  );
  return node;
}

/** Labelled form field. */
function field(labelText, control) {
  const wrapper = element("label", "field");
  wrapper.append(element("span", "", labelText), control);
  return wrapper;
}

function renderComments(list, card, reload) {
  list.replaceChildren();
  for (const comment of card.comments) {
    const item = element("li", "comment");
    item.append(
      element("span", "comment-text", comment.text),
      element("time", "comment-time", comment.created_at),
      iconButton("Delete comment", "✕", async () => {
        await request("DELETE", `/api/comments/${comment.id}`);
        await reload();
        act(async () => {});
      }),
    );
    list.append(item);
  }
}

/** Open the native dialog with the details of one card. */
async function openDetails(cardId) {
  let card;
  try {
    card = await request("GET", `/api/cards/${cardId}`);
  } catch (error) {
    showError(error.message);
    return;
  }
  const dialog = element("dialog", "details");
  const form = element("form", "details-form");
  const title = element("input");
  title.value = card.title;
  const label = element("select");
  for (const name of ["", ...LABELS]) {
    const option = element("option", "", name || "none");
    option.value = name;
    label.append(option);
  }
  label.value = card.label || "";
  const description = element("textarea");
  description.rows = 4;
  description.value = card.description || "";
  const due = element("input");
  due.type = "date";
  due.value = card.due_date || "";
  const done = element("input");
  done.type = "checkbox";
  done.checked = card.done;
  const message = element("div", "dialog-error");
  message.setAttribute("role", "alert");
  const save = element("button", "", "Save");
  save.type = "submit";
  const close = element("button", "", "Close");
  close.type = "button";
  close.addEventListener("click", () => dialog.close());
  const actions = element("div", "dialog-actions");
  actions.append(save, close);
  form.append(
    element("h2", "", "Card details"),
    field("Title", title),
    field("Label", label),
    field("Description", description),
    field("Due date", due),
    field("Done", done),
    message,
    actions,
  );
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    try {
      await request("PATCH", `/api/cards/${cardId}`, {
        title: title.value,
        label: label.value,
        description: description.value,
        due_date: due.value || null,
        done: done.checked,
      });
      dialog.close();
      act(async () => {});
    } catch (error) {
      message.textContent = error.message;
    }
  });
  const comments = element("ul", "comments");
  const reload = async () => {
    card = await request("GET", `/api/cards/${cardId}`);
    renderComments(comments, card, reload);
  };
  renderComments(comments, card, reload);
  const commentForm = element("form", "comment-form");
  const commentInput = element("input");
  commentInput.setAttribute("aria-label", "New comment");
  const commentAdd = element("button", "", "Comment");
  commentAdd.type = "submit";
  commentForm.append(commentInput, commentAdd);
  commentForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    try {
      await request("POST", `/api/cards/${cardId}/comments`, { text: commentInput.value });
      commentInput.value = "";
      message.textContent = "";
      await reload();
      act(async () => {});
    } catch (error) {
      message.textContent = error.message;
    }
  });
  dialog.append(form, element("h3", "", "Comments"), comments, commentForm);
  dialog.addEventListener("close", () => dialog.remove());
  document.body.append(dialog);
  dialog.showModal();
}

function renderList(list) {
  const section = element("section", "list");
  section.dataset.listId = String(list.id);
  section.addEventListener("dragover", (event) => overList(event, section));
  section.addEventListener("dragleave", () => section.classList.remove("drop-target"));
  section.addEventListener("drop", (event) => dropOnList(event, list.id, section));
  const header = element("div", "list-header");
  header.draggable = true;
  header.addEventListener("dragstart", (event) => startDrag(event, "list", list.id, section));
  header.addEventListener("dragend", endDrag);
  const title = element("h2", "", list.name);
  header.append(
    title,
    iconButton(`Rename list ${list.name}`, "✎", () =>
      inlineForm(title, list.name, "Save", (value) =>
        act(() => request("PATCH", `/api/lists/${list.id}`, { name: value })), "List name")),
    iconButton(`Delete list ${list.name}`, "✕", () =>
      act(() => request("DELETE", `/api/lists/${list.id}`))),
  );
  section.append(header);
  for (const card of list.cards) {
    section.append(renderCard(card));
  }
  const add = element("button", "add-button", "+ Add a card");
  add.type = "button";
  add.addEventListener("click", () =>
    inlineForm(add, "", "Add", (value) =>
      act(() => request("POST", `/api/lists/${list.id}/cards`, { title: value })), "Card title"));
  section.append(add);
  return section;
}

function renderAddList() {
  const box = element("div", "add-list");
  const add = element("button", "add-button", "+ Add another list");
  add.type = "button";
  add.addEventListener("click", () =>
    inlineForm(add, "", "Add list", (value) =>
      act(() => request("POST", "/api/lists", { board_id: state.board.id, name: value })), "List name"));
  box.append(add);
  return box;
}

/** Drag and drop with the browser's native events. */
const drag = { kind: null, id: null };

function startDrag(event, kind, id, node) {
  event.stopPropagation();
  drag.kind = kind;
  drag.id = id;
  event.dataTransfer.effectAllowed = "move";
  event.dataTransfer.setData("text/plain", `${kind}:${id}`);
  requestAnimationFrame(() => node.classList.add("dragging"));
}

function endDrag() {
  drag.kind = null;
  drag.id = null;
  document.querySelectorAll(".dragging, .drop-target").forEach((node) =>
    node.classList.remove("dragging", "drop-target"));
}

/** Number of items whose centre is before the pointer, not counting the dragged one. */
function insertIndex(container, selector, pointer, vertical) {
  let index = 0;
  for (const item of container.querySelectorAll(selector)) {
    if (item.classList.contains("dragging")) {
      continue;
    }
    const box = item.getBoundingClientRect();
    const centre = vertical ? box.top + box.height / 2 : box.left + box.width / 2;
    if (centre < pointer) {
      index += 1;
    }
  }
  return index;
}

function overList(event, section) {
  if (drag.kind === "card") {
    event.preventDefault();
    section.classList.add("drop-target");
  }
}

function dropOnList(event, listId, section) {
  if (drag.kind !== "card") {
    return;
  }
  event.preventDefault();
  const cardId = drag.id;
  const position = insertIndex(section, ".card", event.clientY, true);
  endDrag();
  act(() => request("PATCH", `/api/cards/${cardId}/move`, { list_id: listId, position }));
}

function enableListDrop(main) {
  main.addEventListener("dragover", (event) => {
    if (drag.kind === "list") {
      event.preventDefault();
    }
  });
  main.addEventListener("drop", (event) => {
    if (drag.kind !== "list") {
      return;
    }
    event.preventDefault();
    const listId = drag.id;
    const position = insertIndex(main, ".list", event.clientX, false);
    endDrag();
    act(() => request("PATCH", `/api/lists/${listId}/move`, { position }));
  });
}

function render() {
  const main = document.getElementById("board");
  main.replaceChildren(...state.board.lists.map(renderList), renderAddList());
}

enableListDrop(document.getElementById("board"));
act(async () => {});
