[English](Step-5-Card-Details) · **Dansk** · [Bahasa Malaysia](Step-5-Card-Details-ms)

# Trin 5: Kortdetaljer

![Trin 5: dialogen med kortets detaljer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-05.png)

## Hvad vi byggede

Et kort er nu mere end en titel. Klik på et kort for at åbne en dialog, hvor du sætter en farvet etiket, en beskrivelse, en forfaldsdato og en færdig-markering, og hvor du tilføjer eller sletter tekstkommentarer. På tavlen viser hvert kort en etiketstribe, et beskrivelsesikon, et kommentartal og et mærke med forfaldsdato. Et forfaldent kort har et rødt datomærke, og et færdigt kort er streget over.

## Hvad vi fik ud af det

- **Datamodellering.** Kortet fik fem nye oplysninger: etiket, beskrivelse, forfaldsdato, færdig og kommentarer. Kommentarer er en egen tabel med fremmednøgle og `ON DELETE CASCADE`, så sletning af et kort fjerner dets kommentarer.
- **Validering ét sted.** Reglerne for etiket (en fast palet), længden af beskrivelse og kommentar og forfaldsdatoen ligger i `domain/detail_rules.py`. En forkert værdi giver en domænefejl, og routeren svarer 400.
- **Datoer.** En forfaldsdato er en almindelig streng `ÅÅÅÅ-MM-DD`. `datetime.date.fromisoformat` er for eftergivende, så reglen tjekker også formen; 2026-02-30 afvises. Browseren afgør forfaldent ved at sammenligne strengen med dagens dato.
- **En migrering.** Når en database fra et tidligere trin åbnes, tilføjes de nye kolonner og kommentartabellen, og `PRAGMA user_version` sættes, så ingen data går tabt.
- **En delvis opdatering.** `PATCH /api/cards/{id}` ændrer kun de felter, der sendes; `due_date: null` fjerner datoen.
- **En indbygget dialog.** Elementet `dialog` giver fokushåndtering, Escape til at lukke og en baggrund uden et bibliotek.
