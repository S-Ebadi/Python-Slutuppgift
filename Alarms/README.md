# README – Alarms/alarms.py

Den här filen förklarar exakt vad som händer i koden för alarms.py och hur klasserna och funktionerna samverkar.

## Syfte
alarms.py hanterar all logik kring larm i systemmonitor-projektet. Här skapas, sparas, laddas och triggas larm för CPU, minne och disk.

## Klasser och funktioner

### AlarmType (enum)
- Håller ordning på vilka typer av larm som finns: CPU, MINNE, DISK.
- Används för att undvika stavfel och för att enkelt kunna utöka med fler larmtyper.

### Alarm (dataklass)
- Beskriver ett larm: vilken typ (CPU/MINNE/DISK) och vilken tröskel (t.ex. 80%).
- Gör det enkelt att skapa, jämföra och sortera larm.

### AlarmManager
- "Larmchefen" som håller koll på alla larm i en lista.
- Kan ladda larm från fil (alarms.json) och spara dem automatiskt när något ändras.
- add_alarm: Lägger till ett nytt larm och sorterar listan.
- remove_alarm: Tar bort ett larm.
- list_sorted: Returnerar alla larm sorterade på typ och tröskel.
- check_triggers: Kollar om någon resurs (CPU, minne, disk) har passerat en larmtröskel och returnerar varningsmeddelanden. Endast det närmaste larmet av en viss typ aktiveras.

## Hur används det?
- När programmet startar laddas alla sparade larm automatiskt.
- Användaren kan skapa och ta bort larm via menyn.
- Vid övervakning kollar AlarmManager om någon resurs har passerat en larmgräns och skriver ut en varning.
- Alla ändringar sparas direkt till alarms.json.

## Varför denna struktur?
- Tydlig separation av ansvar: all larmhantering på ett ställe.
- Lätt att bygga ut med fler larmtyper eller funktioner.
- Robust och enkel att testa.

**Sammanfattning:**
alarms.py är hjärtat för all larmhantering i projektet. Den ser till att inget larm glöms bort och att användaren alltid får veta om något är på väg att gå fel i systemet.
