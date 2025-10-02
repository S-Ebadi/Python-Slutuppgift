
# Systemmonitor

> **En professionell systemmonitor i Python som övervakar CPU, RAM och disk.**  
> *Utvecklad som slutuppgift i kursen Systemutveckling i Python (DevOps-utbildning).*

*Forza Inter 🖤💙*

</div>

---

## Projektbeskrivning

Systemmonitor är ett robust övervakningsverktyg som kontinuerligt analyserar systemresurser med hjälp av biblioteket **psutil**.

### Huvudfunktioner

| Funktion | Beskrivning |
|----------|-------------|
| **Övervakning** | Startar kontinuerlig övervakning av systemresurser |
| **Statusrapporter** | Listar aktuell status för CPU, RAM och diskanvändning |
| **Larmhantering** | Skapar intelligenta larm när fördefinierade gränser passeras |
| **Persistens** | Sparar larm i JSON-format som bevaras mellan sessioner |

---

## Arkitektur

Projektet följer en modulär arkitektur för optimal underhållbarhet och skalbarhet:

```
systemmonitor/
├── main.py        # Startpunkt, håller ihop programmet
├── menu.py        # Meny och input från användaren  
├── monitor.py     # Funktioner som använder psutil
├── alarms.py      # Larmklasser + JSON-hantering
├── utils.py       # Hjälpfunktioner
└── alarms.json    # Fil där larm sparas
```

### Design Filosofi

Syftet är att dela upp koden i **moduler** enligt principen *Separation of Concerns*.  
Detta gör programmet lättare att förstå, ändra och testa.

---

## Vanliga Frågor & Svar

<details>
<summary><strong>Kan du förklara vad koden gör?</strong></summary>

Den övervakar systemresurser. Programmet mäter CPU, RAM och disk, visar status i konsolen och sparar larm i en JSON-fil när gränser passeras.

</details>

<details>
<summary><strong>Varför är arkitekturen uppdelad så här?</strong></summary>

För att separera ansvar. Meny för input, monitor för mätning, alarms för logik, utils för stöd.  
**Typiskt DevOps-tänk: Separation of concerns.**

</details>

<details>
<summary><strong>Varför används psutil?</strong></summary>

För att enkelt hämta systemdata i Python:

```python
import psutil
print(psutil.cpu_percent())
```

</details>

<details>
<summary><strong>Varför sparas larm i JSON?</strong></summary>

För att de ska finnas kvar mellan körningar. JSON är både lättläst för människor och enkelt att hantera i Python:

```python
import json
with open("alarms.json", "w") as f:
    json.dump({"cpu": "80%"}, f)
```

</details>
<details>
<summary><strong>Vad händer om psutil inte är installerat?</strong></summary>

Programmet kraschar vid import. **Lösning:** Definiera beroenden i `requirements.txt`.

</details>

<details>
<summary><strong>Vad händer om alarms.json är korrupt eller saknas?</strong></summary>

Då får man fel vid load. En lösning är att skapa en ny tom fil automatiskt.

</details>

<details>
<summary><strong>Hur testades koden?</strong></summary>

Genom systematiska manuella tester i terminalen:

- ✓ Startade övervakning
- ✓ Triggade larm  
- ✓ Kollade att JSON uppdaterades

</details>

<details>
<summary><strong>Vad händer om CPU ligger konstant högt?</strong></summary>

Då triggas flera larm. I en vidareutveckling kan man sätta rate limiting (t.ex. ett larm per minut).

</details>

<details>
<summary><strong>Största svagheten i programmet just nu?</strong></summary>

Att den inte loggar historisk data. Den visar bara nuvarande status.

</details>

<details>
<summary><strong>Hur kan programmet vidareutvecklas?</strong></summary>

### Framtida Utvecklingsmöjligheter

- 📊 **Historikloggning** - Lagra data i fil/databas
- 🌐 **Web Dashboard** - Bygga gränssnitt med Flask
- 📱 **Notifieringar** - Koppla larm till Slack/Teams  
- 🐳 **Containerisering** - Dockerisera och skicka metrik till Prometheus/Grafana

</details>

<details>
<summary><strong>Kan du visa ett kodexempel på en funktion?</strong></summary>

Ja, här är en funktion från `monitor.py`:

```python
import psutil

def read_memory():
    return psutil.virtual_memory()

print(read_memory())
```

</details>

<details>
<summary><strong>Varför är detta relevant i DevOps?</strong></summary>

För att **övervakning är en kärnuppgift i DevOps**.  
Den här uppgiften är en förenklad övning som tränar på just grunden: mäta resurser, hantera larm och strukturera kod modulärt.

</details>

---

## Installation & Användning

### Systemkrav
- **Python:** 3.8 eller senare
- **Operativsystem:** Windows, macOS, Linux
- **Beroenden:** Se `requirements.txt`

### Snabb Start

1. **Klona repository**
   ```bash
   git clone https://github.com/[S-Ebadi]/systemmonitor.git
   cd systemmonitor
   ```

2. **Installera beroenden**
   ```bash
   pip install -r requirements.txt
   ```

3. **Starta programmet**
   ```bash
   python main.py
   ```

### Användargränssnitt
Programmet erbjuder en intuitiv meny med följande alternativ:
- Visa aktuell systemstatus
- Konfigurera övervakningslarm  
- Hantera befintliga larm
- Starta kontinuerlig övervakning

---

<div align="center">

   **DevOps** ❤️ 

### *Passion för automatisering, övervakning och kontinuerlig förbättring*

**┌────────────────────────────────────────┐**  
**│          Made with 💜 for DevOps       │**  
**└────────────────────────────────────────┘**


</div>

