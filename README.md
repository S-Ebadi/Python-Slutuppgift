
# Systemmonitor

**Håll koll på din dators prestanda i realtid.**

Ett enkelt Python-program som övervakar CPU, minne och disk. Skapa larm, få notifieringar när något går fel, och spara allt för senare analys.

*Forza Inter 🖤💙*

</div>

---

## Vad gör programmet?

Systemmonitor visar live-data från din dator och varnar dig när resurser börjar ta slut. Perfekt för att förstå systembelastning eller testa prestanda under olika förhållanden.

### Huvudfunktioner

| Funktion | Beskrivning |
|----------|-------------|
| **Realtidsövervakning** | Kontinuerlig övervakning med live-uppdatering av CPU, minne och disk |
| **Intelligent larmhantering** | Konfigurera, redigera och ta bort larm med tröskelvärdeskontroll |
| **Sessionsloggning** | Automatisk JSON-loggning av alla mätpunkter och larm |
| **Ljudalarmer** | Audiovisuella signaler vid larmtrigger med beep-funktionalitet |
| **Historikanalys** | Visa resultat från tidigare övervakningssessioner |
| **Modulär arkitektur** | Separata moduler för olika ansvarsområden |

---

## Arkitektur

Projektet implementerar en ren modulär arkitektur med tydlig separation av ansvar:

```
Systemmonitor/
├── main.py           # Huvudapplikation med menyhantering och orchestrering
├── monitor.py        # Systemresursmätning via psutil
├── alarms.py         # Komplett larmhantering med JSON-persistens
├── utils.py          # Hjälpfunktioner för formatting, input och ljud
├── requirements.txt  # Beroenden (psutil==7.1.0)
├── alarms.json      # Dynamisk larmlagring
└── Storage/
    └── session-*.json # Automatisk sessionsloggning
```

### Designprinciper

- **Separation of Concerns**: Varje modul har ett tydligt ansvarsområde
- **Single Responsibility**: Funktioner fokuserar på en uppgift
- **Dependency Injection**: Moduler importerar endast vad de behöver
- **Data Persistence**: JSON-baserad lagring för larm och sessionsloggar

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
def cpu():     # Returnerar CPU-användning i procent
def mem():     # Returnerar minnesstatus (procent, använt, totalt)
def disk():    # Returnerar diskstatus (procent, använt, totalt)
```

### Larmhantering (alarms.py)
Komplett CRUD-funktionalitet för larmhantering:

- **Skapa larm**: `create(metric, threshold, direction)` med UUID-generering
- **Lista larm**: `list_all()` returnerar alla konfigurerade larm
- **Uppdatera larm**: `update(id, **kwargs)` för att ändra befintliga larm
- **Ta bort larm**: `delete(id)` för att radera specifika larm
- **Evaluera larm**: `evaluate(cpu, mem, disk)` kontrollerar tröskelöverskridanden

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

**Larmlagring** (`alarms.json`):
```json
{
  "id": "uuid-string",
  "metric": "cpu|memory|disk", 
  "threshold": 75.0,
  "direction": ">="
}
```

**Sessionsloggning** (`Storage/session-YYYYMMDD-HHMMSS.json`):
```json
{
  "cpu": 100.0,
  "mem": 70.1, 
  "disk": 6.8,
  "alarms": ["LARM: CPU >= 75%"],
  "timestamp": "2025-10-02 19:29:19"
}
```

---

## Vanliga Frågor & Svar

<details>
<summary><strong>Vad gör programmet exakt?</strong></summary>

Programmet övervakar CPU, minne och disk i realtid. Det visar live-data i terminalen, triggar larm när gränser passeras, spelar ljudsignaler och sparar all data i JSON-format för senare analys.

</details>

<details>
<summary><strong>Hur fungerar larmhanteringen?</strong></summary>

Larm konfigureras med tröskelväden (1-100%). Systemet kontrollerar kontinuerligt alla larm och triggar när värden överstiger gränserna. Varje larm får ett unikt UUID och sparas persistent i `alarms.json`.

</details>

<details>
<summary><strong>Vad sparas i Storage-mappen?</strong></summary>

Varje övervakningssession genererar en JSON-fil med alla mätpunkter, triggade larm och tidsstämplar. Detta möjliggör historisk analys och trendspårning.

</details>

<details>
<summary><strong>Hur använder programmet psutil?</strong></summary>

```python
import psutil

def cpu(): return psutil.cpu_percent(interval=1)
def mem(): return psutil.virtual_memory().percent, used, total  
def disk(): return psutil.disk_usage("/").percent, used, total
```

</details>

<details>
<summary><strong>Vad händer vid larmtrigger?</strong></summary>

Vid larmtrigger händer två saker samtidigt:
1. Meddelande visas i terminalen: `*** LARM: CPU >= 75% ***`
2. Larmet loggas i sessionsdata för senare analys

**Observera**: Ljudfunktionalitet (`utils.beep()`) är implementerad men används inte i denna slutuppgift.

</details>

<details>
<summary><strong>Kan man redigera befintliga larm?</strong></summary>

Ja, via menyn "Ändra/Ta bort larm" kan du:
- Ändra tröskelväden för befintliga larm
- Ta bort larm helt från systemet
- Alla ändringar sparas omedelbart till `alarms.json`

</details>

---

## Installation & Användning

### Systemkrav
- **Python:** 3.8+ med psutil-stöd
- **Operativsystem:** Windows, macOS, Linux (Unix-kompatibel)
- **Terminal:** Stöd för ANSI escape codes och audio (\a)
- **Beroenden:** `psutil==7.1.0` (specificerat i requirements.txt)

### Installation

1. **Klona eller ladda ner projektmappen**
   ```bash
   cd Systemmonitor/
   ```

2. **Installera psutil**
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Verifiera installation**
   ```bash
   python -c "import psutil; print('psutil version:', psutil.__version__)"
   ```

### Körning

**Starta huvudprogrammet:**
```bash
python main.py
```

**Förväntad output:**
```
=== Huvudmeny ===
1. Starta övervakning
2. Lista aktiv övervakning  
3. Skapa larm
4. Visa larm
5. Ändra/Ta bort larm
6. Visa senaste övervakningsresultat
7. Avsluta
Välj: 
```

### Användningsexempel

**Steg 1 - Skapa ett larm:**
- Välj alternativ `3`
- Välj `1` för CPU-larm  
- Ange tröskel t.ex. `80`
- Larmet sparas automatiskt i `alarms.json`

**Steg 2 - Starta övervakning:**
- Välj alternativ `1` 
- Se realtidsdata: `CPU 45% | Minne 67% (5.2 GB / 8.0 GB) | Disk 23% (45.6 GB / 200.0 GB)`
- När CPU > 80%: `*** LARM: CPU >= 80% ***` visas i terminalen
- Tryck Enter för att stoppa

**Steg 3 - Analysera sessionen:**
- Välj alternativ `6`
- Se sammanfattning av senaste körningen
- Kontrollera antal mätpunkter och triggade larm

### Filstruktur efter körning

```
Systemmonitor/
├── main.py
├── monitor.py  
├── alarms.py
├── utils.py
├── requirements.txt
├── alarms.json              # Dina sparade larm
└── Storage/
    └── session-20251002-192929.json  # Automatisk sessionslogg
```

---
