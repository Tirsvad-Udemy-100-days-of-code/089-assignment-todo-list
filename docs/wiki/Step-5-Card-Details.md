**English** · [Dansk](Step-5-Card-Details-da) · [Bahasa Malaysia](Step-5-Card-Details-ms)

# Step 5: Card details

![Step 5: the card detail dialog](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-05.png)

## What we built

A card is now more than a title. Click a card to open a dialog where you set a coloured label, a description, a due date and a done state, and where you add or delete text comments. On the board each card shows a label bar, a description icon, a comment count and a due date badge. An overdue card has a red date badge and a done card is crossed out.

## What we gained

- **Data modelling.** The card gained five facts: label, description, due date, done and comments. Comments are their own table with a foreign key and `ON DELETE CASCADE`, so deleting a card removes its comments.
- **Validation in one place.** The rules for label (a fixed palette), description and comment length, and the due date live in `domain/detail_rules.py`. A broken value raises a domain error and the router answers 400.
- **Dates.** A due date is a plain `YYYY-MM-DD` string. `datetime.date.fromisoformat` is too forgiving, so the rule also checks the shape; 2026-02-30 is rejected. The browser decides overdue by comparing the string to today's date.
- **A migration.** Opening a database from an earlier step adds the new columns and the comments table and sets `PRAGMA user_version`, so no data is lost.
- **A partial update.** `PATCH /api/cards/{id}` changes only the fields that are sent; `due_date: null` clears the date.
- **A native dialog.** The `dialog` element gives focus handling, Escape to close and a backdrop with no library.
