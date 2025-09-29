# README – Main

Den här mappen innehåller programmets startpunkt och logik för att starta hela systemmonitor-applikationen.

## Syfte
main.py är det första som körs när du startar programmet. Här skapas loggfilen, larm laddas in och huvudmenyn startas.

## Viktiga delar
- **main.py**: Skapar logg, laddar larm via AlarmManager och startar menyn (Menu).
- **Logger**: Ser till att allt viktigt loggas till fil, så att du kan följa vad som händer.

## Hur används det?
- Kör `python Main/main.py` för att starta hela programmet.
- Allt annat (meny, larm, övervakning) startas härifrån.

**Sammanfattning:**
Main-mappen är navet som kopplar ihop alla delar och ser till att programmet startar på rätt sätt.
