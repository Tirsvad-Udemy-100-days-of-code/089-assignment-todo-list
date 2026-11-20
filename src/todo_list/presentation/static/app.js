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

function renderCard(card) {
  const node = element("div", "card");
  const title = element("span", "card-title", card.title);
  node.append(
    title,
    iconButton(`Rename card ${card.title}`, "✎", () =>
      inlineForm(title, card.title, "Save", (value) =>
        act(() => request("PATCH", `/api/cards/${card.id}`, { title: value })), "Card title")),
    iconButton(`Delete card ${card.title}`, "✕", () =>
      act(() => request("DELETE", `/api/cards/${card.id}`))),
  );
  return node;
}

function renderList(list) {
  const section = element("section", "list");
  const header = element("div", "list-header");
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

function render() {
  const main = document.getElementById("board");
  main.replaceChildren(...state.board.lists.map(renderList), renderAddList());
}

act(async () => {});
