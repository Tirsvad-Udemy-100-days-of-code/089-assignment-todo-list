[English](Step-1-Foundation) · **Dansk** · [Bahasa Malaysia](Step-1-Foundation-ms)

# Trin 1: Projektets fundament

![Trin 1: den første side med fem tomme lister](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-01.png)

## Hvad vi byggede

Et konfigureret Python-projekt, der viser en første side: en blå tavle med fem tomme lister med navnene Backlog, To Do, In Progress, Review og Done.

## Hvad vi fik ud af det

- **Et lokalt virtuelt miljø.** `python -m venv .venv` holder projektets pakker adskilt fra systemets Python, og `python -m pip install --upgrade pip` holder pip opdateret.
- **Én projektfil.** `pyproject.toml` rummer Python-versionen (3.13 eller nyere), den tomme liste af afhængigheder og indstillingerne for pytest, ruff og mypy.
- **Konstanter ét sted.** `constants.py` rummer alle faste værdier, så en ændring kun sker ét sted.
- **Lag.** `domain`, `application`, `infrastructure` og `presentation` holder reglerne adskilt fra databasen og nettet; afhængighederne peger indad.
- **MVC til nettet.** En controller svarer på forespørgslen, og en view bygger HTML.
- **Tests først.** pytest kører enhedstests af viewet og integrationstests af en rigtig server på en fri port.
- **Dokumentation fra kildekoden.** Doxygen-kommentarer og en `Doxyfile` bygger kodedokumentationen.
- **Sikre skærmbilleder.** En Docker-container med en browser uden skærm tager billedet, så skrivebordet aldrig bruges.
- **Et tjek før hvert push.** opengrep tjekker koden mod lokale regler.
