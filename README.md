# pingis-stats

Hej! Här kan vi diskutera, planera och så utveckla vår app för att tracka och följa upp pingisspelandet på kontoret.
Grundiden är att ha en dator/skärm av något slag vid pingisbordet där man kan registrera sig själv som spelare, samt matcher som spelas. Den ska även ha någon slags dashboard där man kan följa upp spelares utveckling och matchstatistik etc.
Kom gärna med ideer, förslag och kommentarer udner fliken `Issues`.


## Implementation

Min första draft på grundsystemet ser ut enligt bilden. Jag har börjat sätta upp de olika delarna lokalt enligt följande:
- data_pipeline: python
- players, matches: postgres databas
- input_results: Flask web app
 
Sedan tänker jag som första förslag en Power BI dashboard som kan visualisera följande:
- Utveckling av spelares ranking
- Jämförelse av olika spelare
- Hur många matcher som spelas
- Vem som är bra mot vem
- osv...

Mer detaljer om dessa delar finns under `Issues`, en issue för varje del.
Se även den preliminära datamodellen för systemet [här](https://github.com/RikardMartin/pingis-stats/blob/main/docs/system_chart.md)

 
## Några frågor jag vill reda ut är:
- Är implementationsstacken bra?
- Hur ska det deployas? (lokalt på dator? cloud webservice?)
- Hur ska vi arbeta med projektet? (Upwards together?)
