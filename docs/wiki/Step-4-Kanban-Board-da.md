[English](Step-4-Kanban-Board) · **Dansk** · [Bahasa Malaysia](Step-4-Kanban-Board-ms)

# Trin 4: Kanban-tavle og træk og slip

![Trin 4: et kort trukket fra To Do til Review](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-04.png)

## Hvad vi byggede

Tavlen opfører sig nu som en Kanban-tavle. Kort flyttes mellem lister og inden for en liste, og lister flyttes til venstre og højre, alt med træk og slip. Hver flytning gemmes: efter en genindlæsning ser tavlen ens ud.

Tegningen, der styrede udseendet (blå baggrund, afrundede listekolonner, hvide kort og en Add a card-knap under hver liste):

![Tegning af tavlen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/wireframes/board.svg)

## Hvad vi fik ud af det

- **To flytte-endepunkter.** `PATCH /api/cards/{id}/move` tager `list_id` og `position`; `PATCH /api/lists/{id}/move` tager `position`. Lageret omnummererer naboerne i én transaktion, så placeringer aldrig har huller, og en placering forbi enden betyder enden.
- **Indbygget træk og slip.** Browserens hændelser `dragstart`, `dragover` og `drop` er nok. Placeringen er antallet af kort, hvis midte er over musen.
- **Visuel tilbagemelding.** Et trukket kort bliver bleg, og listen under musen får en stiplet kant.
- **Et responsivt layout.** Tavlen ruller sidelæns på smalle skærme, og lister bliver aldrig bredere end skærmen.
- **Browsertests af træk.** Tests i en Docker-container trækker et kort og en liste og tjekker rækkefølgen efter en genindlæsning.
