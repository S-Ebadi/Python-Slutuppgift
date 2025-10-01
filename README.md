
# Slutuppgift

Syftet med slutuppgiften är att bygga ett enkelt men komplett Python program som övervakar datorns resurser (CPU, minne, disk) och larmar när fördefinierade gränser överskrids. Lösningen ska vara robust, användarvänlig och visa grundläggande förståelse för modulär programmering, filhantering och systemintegration.

## Min lösning: Systemmonitor

Systemmonitor är en konsolapplikation som:

- Visar aktuell status för CPU, minne och disk.
- Låter användaren skapa och ta bort larm för olika resurser.
- Sparar larm till fil (`alarms.json`) och laddar dem automatiskt vid start.
- Loggar viktiga händelser till fil.
- Har en tydlig meny med validerad inmatning.

### Projektstruktur

```text
systemmonitor/
├─ main.py          # Huvudprogrammet med menyn (5 val)
├─ monitor.py       # Hämtar CPU, minne och disk via psutil
├─ alarms.py        # Alarm-klass + lagring och JSON-hantering
├─ utils.py         # Hjälpfunktioner för input, enter-loop, formattering
├─ requirements.txt # psutil>=7.1.0
└─ alarms.json      # Skapas/uppdateras automatiskt, sparar larm mellan körningar
```

### Installation

1. Klona projektet:
   ```bash
   git clone <repo-url>
   cd Systemmonitor
   ```
2. Installera beroenden:
   ```bash
   pip install -r requirements.txt
   ```

### Användning

Starta programmet:

```bash
python3 main.py
```

Du får en meny med:

1. Visa status
2. Konfigurera larm
3. Visa larm
4. Starta övervakning
5. Avsluta

Följ instruktionerna i konsolen. Alla inmatningar kontrolleras och fel hanteras.

### Loggning och larm

- Händelser loggas till `systemmonitor.log`.
- Larm sparas i `alarms.json` och laddas automatiskt.
- Du kan skapa och ta bort larm via menyn.

### Reflektion kring utmaningar och genombrott

- Hur man delar upp kod i moduler och hanterar filimporter.
- Hur man använder externa bibliotek (psutil) för systeminfo.
- Hur man sparar och laddar data med JSON.
- Hur man bygger en enkel meny och validerar inmatning.
- Hur man loggar händelser och hanterar fel.

Jag har försökt hålla koden så enkel och tydlig som möjligt, men ändå följa uppgiftens krav. Lösningen är robust och lätt att vidareutveckla.

---

> "No man has the right to be an amateur in the matter of physical training. It is a shame for a man to grow old without seeing the beauty and strength of which his body is capable."

— Sokrates
