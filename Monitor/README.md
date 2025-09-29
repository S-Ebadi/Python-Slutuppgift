# README – Monitor

Den här mappen innehåller logik för att läsa av systemets resurser.

## Syfte
Monitor-modulen använder psutil för att hämta aktuell status för CPU, minne och disk.

## Viktiga delar
- **monitor.py**: Innehåller funktioner för att läsa av och presentera systemstatus.

## Hur används det?
- Menu anropar Monitor för att visa status eller kontrollera om larm ska triggas.
- All systemdata hämtas härifrån.

**Sammanfattning:**
Monitor-mappen är "ögonen" i systemet och ser till att vi alltid vet hur datorn mår.
