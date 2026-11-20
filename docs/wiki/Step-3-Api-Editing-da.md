[English](Step-3-Api-Editing) · **Dansk** · [Bahasa Malaysia](Step-3-Api-Editing-ms)

# Trin 3: JSON-API og redigering

![Trin 3: en ny liste og en kortformular](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-03.png)

## Hvad vi byggede

Et JSON-API til lister og kort og en side, der bruger det: man kan oprette, omdøbe og slette lister og kort uden at genindlæse siden. Serveren sender kun et lille HTML-skelet; almindelig JavaScript bygger tavlen.

## API'et

| Metode og sti | Hvad den gør | Succes |
| --- | --- | --- |
| `GET /api/board` | Tavlen med lister og kort | 200 |
| `POST /api/lists` | Opret en liste (`board_id`, `name`) | 201 |
| `PATCH /api/lists/{id}` | Omdøb en liste | 200 |
| `DELETE /api/lists/{id}` | Slet en liste og dens kort | 204 |
| `POST /api/lists/{id}/cards` | Opret et kort (`title`) | 201 |
| `PATCH /api/cards/{id}` | Omdøb et kort | 200 |
| `DELETE /api/cards/{id}` | Slet et kort | 204 |

Fejl er JSON med en `error`-besked: 400 ved et dårligt navn eller indhold, 404 ved et ukendt id eller en ukendt sti, 405 ved en forkert metode. Der sendes aldrig et stack trace.

## Hvad vi fik ud af det

- **En lille router.** Ruter kobler en metode og et stimønster (`{id}`) til en controller-funktion; ét sted gør domænefejl til statuskoder.
- **HTTP i almindelig Python.** `http.server` læser indholdet og skriver svaret; controllerne ser aldrig sockets.
- **Validering i kanten.** `require_str` og `require_int` tjekker hvert JSON-felt, før en handling kører.
- **En side uden framework.** `app.js` bruger `fetch`, bygger DOM med `textContent` (så navne ikke kan indsætte HTML) og tegner igen efter hver ændring.
- **Browsertests uden skrivebordet.** End-to-end-testene kører i en Docker-container med en browser uden skærm og skriver resultatet til en fil.
