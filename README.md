
# Systemmonitor

> **En systemmonitor i Python som öve### Huvudmeny (main.py)
Programmet erbjuder en enkel 4-punktsmeny:

1. **Starta övervakning** - Kontinuerlig realtidsövervakning, avslutas med Ctrl+C
2. **Visa senaste status** - Visar sista mätning från tidigare session
3. **Hantera larm** - Undermeny för att skapa, visa, ändra eller ta bort larm
4. **Avsluta** - Säker avslutning av programmet, RAM och disk.**  
> *Utvecklad som slutuppgift i kursen Systemutveckling i Python (DevOps-utbildning, Chas Academy).*

*Forza Inter 🖤💙*

</div>

---

## Projektbeskrivning

Systemmonitor är ett övervakningsverktyg som mäter systemresurser med hjälp av **psutil**.  
Programmet körs i terminalen och erbjuder både realtidsövervakning, larmhantering och loggning.

### Huvudfunktioner

| Funktion | Beskrivning |
|----------|-------------|
| **Övervakning** | Startar och stoppar aktivt övervakningsläge, avslutas med Enter |
| **Statusrapporter** | Visar aktuell CPU-, RAM- och diskanvändning |
| **Larmhantering** | Skapa, visa, ändra eller ta bort larm för CPU, RAM, disk |
| **Persistens** | Larm sparas i `Storage/alarms.json` och laddas vid programstart |
| **Loggning** | Alla händelser loggas i `Storage/log-*.txt` (med tidsstämpel) |
| **Sessionhistorik** | Varje övervakningssession sparas som `Storage/session-*.json` |
| **Närmaste larm** | Om flera larm finns (60/70/80%), triggas endast det mest relevanta |

---

## Arkitektur

Projektet följer en modulär arkitektur med tydlig separation av ansvar:

```
systemmonitor/
├── main.py        # Huvudprogram, meny och styrning
├── monitor.py     # Resursmätning via psutil (read_cpu, read_memory, read_disk)
├── alarms.py      # AlarmStore-klass för CRUD och persistens
├── utils.py       # Hjälpfunktioner (t.ex. press, beep, validering)
├── logger.py      # Loggar händelser till tidsstämplade loggfiler
└── Storage/       # Datafiler (alarms.json, log-*.txt, session-*.json)
```

### Designfilosofi

- **Separation of Concerns** – varje modul har sitt ansvar  
- **Refaktorering** – mindre kod, samma funktionalitet  
- **DevOps-tänk** – loggning, struktur, felhantering, persistens

---

## Funktionell Specifikation

### Huvudmeny (main.py)
Programmet startar med en interaktiv meny som erbjuder 7 huvudfunktioner:

1. **Starta övervakning** - Kontinuerlig realtidsövervakning med live-display
2. **Lista aktiv övervakning** - Visar nuvarande status för pågående övervakning  
3. **Skapa larm** - Interaktiv guide för att konfigurera nya larm
4. **Visa larm** - Lista alla konfigurerade larm sorterade på typ
5. **Ändra/Ta bort larm** - Redigera befintliga larm eller ta bort dem
6. **Visa senaste övervakningsresultat** - Analys av tidigare sessioner
7. **Avsluta** - Säker avslutning av programmet

### Systemmonitorering (monitor.py)
Modulen använder `psutil` för att hämta systemdata:

```python
def read_cpu():     # Returnerar CPU-användning i procent
def read_memory():  # Returnerar psutil.virtual_memory() objekt
def read_disk():    # Returnerar psutil.disk_usage('/') objekt
```

### Larmhantering (alarms.py)
AlarmStore-klass med komplett CRUD-funktionalitet:

- **Skapa larm**: `add(metric, threshold)` lägger till nya larm
- **Lista larm**: `list()` returnerar alla larm sorterade på typ
- **Uppdatera larm**: `update(index, threshold)` ändrar befintliga larm
- **Ta bort larm**: `remove(index)` raderar specifika larm
- **Evaluera larm**: `get_relevant(metric, value)` hittar närmaste larm

### Hjälpfunktioner (utils.py)
Verktygsmodul med användbara funktioner:

- **Datakonvertering**: `gb(bytes)` - Konverterar bytes till GB
- **Användarinteraktion**: `press()`, `choice()`, `fnum()` för input
- **Visuella effekter**: `spinner()`, `led()`, `clr_line()` för UI
- **Ljudsignaler**: `beep(times, interval)` - Implementerad men ej använd i denna slutuppgift

---

## Dataflöde & Persistence

### Realtidsövervakning
När övervakning aktiveras sker följande:

1. **Threading**: Separata trådar för användarinput och mätningar
2. **Live Display**: Kontinuerlig uppdatering av systemstatus i terminalen
3. **Larmkontroll**: Automatisk evaluering av alla konfigurerade larm
4. **Ljudsignal**: `utils.beep()` aktiveras vid larmtrigger
5. **Loggning**: Varje mätpunkt sparas i session_log med tidsstämpel

### JSON-baserad Lagring

**Larmlagring** (`Storage/alarms.json`):
```json
{
  "metric": "cpu|mem|disk", 
  "threshold": 90.0
}
```

**Sessionsloggning** (`Storage/session-YYYYMMDD-HHMMSS.json`):
```json
{
  "cpu": 99.9,
  "mem": 72.7, 
  "disk": 6.8,
  "timestamp": "2025-10-02 20:47:57"
}
```

**Händelseloggning** (`Storage/log-YYYYMMDD-HHMMSS.txt`):
```
2025-10-02 20:47:56 - Övervakning startad
2025-10-02 20:47:57 - LARM: CPU över 90.0%
2025-10-02 20:48:07 - Övervakning stoppad
```

---

## Vanliga Frågor & Svar

<details>
<summary><strong>Kan du förklara vad koden gör?</strong></summary>

Programmet övervakar CPU-, RAM- och diskanvändning.  
Användaren kan skapa larm som triggas vid en vald gräns.  
Allt sparas i JSON och loggas med tidsstämpel.

</details>

<details>
<summary><strong>Varför är arkitekturen uppdelad så här?</strong></summary>

För att göra programmet mer överskådligt:  
- `main.py` för meny och logik  
- `monitor.py` för mätning  
- `alarms.py` för larmhantering  
- `logger.py` för loggfiler  
- `utils.py` för hjälpmetoder  

Det gör programmet lättare att förstå och vidareutveckla.

</details>

<details>
<summary><strong>Varför används psutil?</strong></summary>

För att enkelt läsa systemets resurser i Python:

```python
import psutil
print(psutil.cpu_percent())
```

</details>

<details>
<summary><strong>Varför sparas larm i JSON?</strong></summary>

För att bevaras mellan körningarna.  
Alla larm sparas i `Storage/alarms.json`.

</details>

<details>
<summary><strong>Vad händer om psutil inte är installerat?</strong></summary>

Programmet kraschar.  
**Lösning:** installera beroenden med `pip install -r requirements.txt`.

</details>

<details>
<summary><strong>Hur testades koden?</strong></summary>

Genom manuella tester i terminalen:
- Starta och stoppa övervakning (skapade 5 mätpunkter)
- Skapa och ta bort larm (CPU 90% triggade 5 gånger)  
- Kontrollera att logg- och sessionsfiler skapades i `Storage/`

</details>

<details>
<summary><strong>Största förbättringen jämfört med tidigare versioner?</strong></summary>

Att programmet nu har:
- OOP via `AlarmStore`-klassen
- Närmaste larm-logik (bara ett triggas åt gången)
- Full loggning och sessionfiler

</details>

<details>
<summary><strong>Hur kan programmet vidareutvecklas?</strong></summary>

- Historisk visualisering av sessioner (grafiskt)
- Notifieringar via Slack/Teams  
- Webbaserad dashboard (Flask + Grafana)
- Docker-stöd för enklare distribution

</details>

---

## Installation & Användning

### Systemkrav
- **Python:** 3.8+
- **OS:** Windows, macOS, Linux
- **Beroenden:** psutil (se requirements.txt)

### Snabbstart

```bash
# Klona repository
git clone https://github.com/S-Ebadi/systemmonitor.git
cd systemmonitor/Systemmonitor

# Installera beroenden
pip install -r requirements.txt

# Starta programmet
python main.py
```

### Menyval

**Huvudmeny:**
1. **Starta övervakning**
2. **Visa senaste status**  
3. **Hantera larm**
4. **Avsluta**

**Larmmeny (alternativ 3):**
1. **Skapa** - Välj CPU/Minne/Disk och sätt tröskel
2. **Visa** - Lista alla aktiva larm
3. **Ändra** - Uppdatera tröskelväden
4. **Ta bort** - Radera specifika larm

---

## Reflektion

Att bygga denna systemmonitor har varit en resa i att hantera mer kod än någonsin tidigare.  
I början kändes mängden överväldigande, men genom att bryta ned allt i moduler och klasser blev det mer hanterbart.

**Jag har lärt mig vikten av:**
- **Struktur** (arkitektur, JSON, loggar)
- **Enkelhet** (refaktorera men bevara funktion)  
- **Helhetstänk** (DevOps handlar om både kod och processer)

Jag har även tagit höjd för funktioner (t.ex. ljud via utils) utan att fullt ut implementera dem, som ett sätt att visa förståelse för hur det kan byggas vidare.

---

<div align="center">

### 🎓 **DevOps Engineering - Class of 2027** ❤️

**┌─────────────────────────────────────────┐**  
**│ 🚀 Chas Academy • Python • Systemutveckling │**  
**│ 💙 Built with passion, powered by coffee   │**  
**│ 🖤 Inter Milano sempre nel cuore           │**  
**└─────────────────────────────────────────┘**



</div>

---
