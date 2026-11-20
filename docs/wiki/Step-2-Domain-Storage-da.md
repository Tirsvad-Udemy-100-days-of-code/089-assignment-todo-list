[English](Step-2-Domain-Storage) · **Dansk** · [Bahasa Malaysia](Step-2-Domain-Storage-ms)

# Trin 2: Domæne og lager

![Trin 2: tavlen læst fra SQLite](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-02.png)

## Hvad vi byggede

Tavlens kerneregler og deres lager. Siden læser nu en tavle fra en SQLite-fil og viser de fem standardlister med deres kort.

## Domænemodellen

| Begreb | Felter | Regler |
| --- | --- | --- |
| Tavle | id, navn | Et nyt lager får én tavle med listerne Backlog, To Do, In Progress, Review og Done |
| Liste | id, tavle, navn, placering | Lister er ordnet fra venstre mod højre; placeringer har ingen huller |
| Kort | id, liste, titel, placering | Kort er ordnet oppefra og ned; et kort er i præcis én liste |

Brugsscenarier: hent tavlen, opret, omdøb, slet og flyt en liste, og opret, omdøb, slet og flyt et kort. Et navn trimmes, må ikke være tomt og har højst 100 tegn.

## Hvad vi fik ud af det

- **Entiteter.** Små uforanderlige dataklasser (`Board`, `CardList`, `Card`) rummer data; listeklassen hedder `CardList`, fordi `list` er en indbygget Python-type.
- **En port.** `BoardRepository` er en `Protocol` i domænet; applikationen afhænger af den og ikke af SQLite.
- **Brugsscenarie-klasser.** Én lille klasse pr. handling med én `execute`-metode.
- **En adapter.** `SqliteBoardRepository` implementerer porten med standardmodulet `sqlite3`, parametriserede forespørgsler og én transaktion pr. kald.
- **To slags tests.** Enhedstests bruger en fake i hukommelsen; integrationstests kører den rigtige adapter på en midlertidig fil. Dækningen er 99 procent.
- **Placeringer uden huller.** Flytning og sletning omnummererer naboerne i samme transaktion.
