
# Systemmonitor – Forza Inter 🖤💙

Ett professionellt verktyg för systemövervakning som ger kontroll över datorns prestanda.  
Mäter CPU-, RAM- och diskanvändning i realtid, hanterar larm och loggar händelser.  
Byggd i Python med hjälp av **psutil**.

*Utvecklad som slutuppgift i kursen Systemutveckling i Python (DevOps-utbildning, Chas Academy).*

---

## Projektbeskrivning

Systemmonitor är ett terminalbaserat övervakningsverktyg som erbjuder:

| Funktion | Beskrivning |
|----------|-------------|
| **Övervakning** | Startar och stoppar aktivt övervakningsläge, avslutas med Enter |
| **Statusrapporter** | Visar nuvarande CPU-, RAM- och diskanvändning |
| **Larmhantering** | Skapa, visa, ändra och ta bort larm (CPU, RAM, Disk) |
| **Persistens** | Larm sparas i `Storage/alarms.json` mellan sessioner |
| **Loggning** | Händelser loggas i `Storage/log-*.txt` med tidsstämpel |
| **Sessionhistorik** | Varje session sparas i `Storage/session-*.json` |
| **Närmaste larm** | Endast det mest relevanta larmet triggas (ex. CPU 80% i stället för 60/70%) |

---

## Arkitektur

Programmet är uppdelat i moduler för tydlighet och underhållbarhet.

```
Systemmonitor/
├── main.py                        # Meny, övervakningslogik och användarflöde
├── monitor.py                     # Funktioner för att mäta CPU, RAM och Disk via psutil
├── alarms.py                      # AlarmStore-klass: skapa, lista, uppdatera, ta bort, evaluera larm
├── utils.py                       # Hjälpfunktioner: input, validering, formatering, UI
├── logger.py                      # Skriver händelser till loggfil med tidsstämpel
├── requirements.txt               # Beroenden (psutil)
├── Storage/                       # Datafiler
│   ├── alarms.json               # Alla aktiva larm
│   ├── session-YYYYMMDD-HHMMSS.json  # Senaste sessionsdata
│   └── log-YYYYMMDD.txt          # Händelselogg
└── Dev-Logg/                     # Personlig utvecklingslogg
```

### Designfilosofi
- **Separation of Concerns**: varje modul har tydligt ansvar.  
- **Persistens**: JSON-filer gör att larm och sessioner bevaras mellan körningar.  
- **Loggning**: händelser spåras med tidsstämpel för transparens.  
- **Enkelhet**: funktionerna hålls små och begripliga.

---

## Funktionell Specifikation

### Huvudmeny (main.py)
Programmet erbjuder dessa alternativ:

1. **Starta övervakning** – kontinuerlig realtidsövervakning med Enter för att stoppa  
2. **Lista aktiv övervakning** – visar status om övervakning är igång  
3. **Skapa larm** – konfigurera CPU-/RAM-/Disklarm (1–100%)  
4. **Visa larm** – lista alla aktiva larm från `Storage/alarms.json`  
5. **Ändra/Ta bort larm** – uppdatera eller ta bort befintliga larm  
6. **Visa senaste övervakning** – summering av senaste session från `Storage/session-*.json`  
7. **Övervakningsläge** – enklare statusläge (utan loggning)  
8. **Avsluta** – stänger programmet

### Monitor (monitor.py)
Ansvarar för att hämta data med **psutil**:
```python
def read_cpu():    # Returnerar CPU-användning i %
def read_memory(): # Returnerar (percent, used, total) för RAM
def read_disk():   # Returnerar (percent, used, total) för disk
```

### Larm (alarms.py)
**AlarmStore**-klass hanterar CRUD för larm:
- `create(metric, threshold, direction)` – skapa nytt larm  
- `list_all()` – lista alla larm  
- `update(id, threshold)` – ändra ett larm  
- `delete(id)` – ta bort larm  
- `evaluate(cpu, mem, disk)` – kolla aktiva larm och trigga relevanta  

### Hjälpfunktioner (utils.py)
- `gb(bytes)` – konverterar bytes till GB  
- `press()` – väntar på Enter  
- `choice()` – validerar menyval  
- `fnum()` – validerar nummer  
- `spinner()`, `led()`, `clr_line()` – UI-finesser  

### Loggning (logger.py)
- Skapar en loggfil i `Storage/` med tidsstämpel i namnet  
- Exempel: `log-20251002-204756.txt`  
- Loggar: programstart, larmtriggers, avslut

---

## Dataflöde & Persistens

### Sessionsdata
Varje övervakning sparas i `Storage/session-*.json` med mätpunkter och triggat larm.

Exempel:
```json
{
  "cpu": 99.9,
  "mem": 72.7,
  "disk": 6.8,
  "alarms": ["CPU över 90%"],
  "timestamp": "2025-10-02 20:47:57"
}
```

### Händelselogg
Skrivs till `Storage/log-*.txt`:
```
2025-10-02 20:47:56 - Övervakning startad
2025-10-02 20:47:57 - LARM: CPU över 90%
2025-10-02 20:48:07 - Övervakning stoppad
```

---

## Vanliga Frågor & Svar

<details>
<summary><strong>Kan du förklara vad koden gör?</strong></summary>
Programmet övervakar CPU, RAM och disk.  
Användaren kan skapa larm, och om gränsen nås triggas larm i terminalen och loggas i JSON/textfil.
</details>

<details>
<summary><strong>Varför är arkitekturen uppdelad så här?</strong></summary>
För att separera ansvar:  
- `main.py` för meny och användarflöde  
- `monitor.py` för mätningar  
- `alarms.py` för larmhantering  
- `utils.py` för input och UI  
- `logger.py` för loggning  
Det gör koden lättare att förstå och ändra.
</details>

<details>
<summary><strong>Varför används psutil?</strong></summary>
För att enkelt läsa systemdata i Python:
```python
import psutil
print(psutil.cpu_percent())
```
</details>

<details>
<summary><strong>Varför sparas larm i JSON?</strong></summary>
För att larm ska finnas kvar mellan körningar. Alla larm sparas i `Storage/alarms.json`.
</details>

<details>
<summary><strong>Vad händer om psutil inte är installerat?</strong></summary>
Programmet kraschar.  
**Lösning:** installera beroenden med `pip install -r requirements.txt`.
</details>

<details>
<summary><strong>Hur testades koden?</strong></summary>
Genom manuella tester i terminalen:  
- Starta och stoppa övervakning  
- Skapa och ta bort larm  
- Kontrollera att logg- och sessionsfiler sparades i `Storage/`
</details>

<details>
<summary><strong>Största förbättringen jämfört med första versionen?</strong></summary>
Att systemet nu har:  
- Larm som sparas mellan sessioner  
- Fullständig loggning av händelser  
- Närmaste larm logik (bara ett triggas åt gången)  
- Sessionsfiler för analys i efterhand
</details>

<details>
<summary><strong>Hur kan programmet vidareutvecklas?</strong></summary>
- Historisk visualisering (grafer)  
- Slack/Teams-notifieringar  
- Webbaserad dashboard (Flask/Grafana)  
- Docker-containerisering
</details>

---

## Installation & Körning

### Systemkrav
- Python 3.8+  
- OS: Windows/macOS/Linux  
- Beroenden: `psutil`  

### Körning
```bash
# Klona repo
git clone https://github.com/S-Ebadi/systemmonitor.git
cd systemmonitor/Systemmonitor

# Installera beroenden
pip install -r requirements.txt

# Starta
python3 main.py
```

---

## Reflektion

Att bygga systemmonitorn har varit en resa i att förstå Python på djupet:  
- **Struktur**: vikten av moduler, loggar och JSON  
- **Enkelhet**: refaktorering utan att tappa funktionalitet  
- **Helhetstänk**: DevOps handlar om både kod, verktyg och process  

Jag har lärt mig att bryta ner ett komplext projekt i tydliga delar och sedan sätta ihop det till en helhet.  
Det gör att jag kan förklara både *vad* koden gör och *varför* den är uppbyggd på detta sätt.

---

### Hälsning
Jag vill avsluta med att säga:  
**Jag hejar på alla i DevOps-25-kullen på Chas Academy ❤️**
