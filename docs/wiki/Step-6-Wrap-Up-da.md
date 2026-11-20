[English](Step-6-Wrap-Up) · **Dansk** · [Bahasa Malaysia](Step-6-Wrap-Up-ms)

# Trin 6: Afslutning og refleksion

![Trin 6: den færdige tavle](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/089-assignment-todo-list/raw/branch/main/docs/screenshots/step-06.png)

## Hvad vi byggede

Det sidste trin tilføjer ingen funktion. Det tjekker, at hele projektet virker for dem, det er til: en kursist, der kloner det, opretter en `.venv`, kører testene og starter tavlen, og en besøgende, der kun læser beskrivelsen, README og denne wiki. Det fulde kvalitetstjek (test, dækning, browsertestene i en container, kildedokumentationen, kodescanningen og rammeværkets kontroller) kørte på den endelige kode.

## Hvad vi fik ud af det

- **Et projekt, der kan afleveres.** README's opsætning blev fulgt bogstaveligt i en ren container.
- **Ét sæt sider på tre sprog** med en sidebjælke og en sproglinje på hver side.
- **En refleksion** (nedenfor), der nævner, hvad der var let, hvad der var svært, og hvad vi ville ændre.

## Refleksion

- **Fremgangsmåde.** Planlæg først: en business case, interessenter, en projektplan og seks milepæle blev godkendt, før den første kodelinje. Hver milepæl var én gren, ét review og én pull request, og hvert trin gav et skærmbillede og en wikiside.
- **Det lette.** Domænereglerne og SQLite. En tavle, lister og kort er en lille model, og lagene holdt reglerne fri for HTTP og SQL, så de fleste test kørte på millisekunder mod et lager i hukommelsen.
- **Det svære.** Træk og slip. Browserens hændelser er lavniveau: slippositionen skal beregnes ud fra markøren, og en test skal trække i en rigtig browser. Datoer var også sværere end ventet, fordi en eftergivende parser accepterer former, man ikke vil have.
- **Største læring.** Et rammeværk er et valg med en pris. Standardbiblioteket (`http.server`, `sqlite3`) var nok, så projektet har ingen afhængigheder ved kørsel, og læseren ser hvert lag. Et webrammeværk ville have sparet routingkode, men også skjult lektionen.
- **Hvad vi ville gøre anderledes.** Starte browsertestene tidligere, give routeren en lille testtabel fra dag ét og vælge teknologi sammen med brugeren før den første milepæl, så en sen ombestemmelse ikke koster noget.
