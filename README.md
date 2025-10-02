
# Systemmonitor

En enkel systemmonitor i **Python** som övervakar CPU, RAM och disk.  
Byggd som slutuppgift i kursen *Systemutveckling i Python* (DevOps-utbildning).  

---

## Projektbeskrivning
Programmet övervakar systemresurser med hjälp av biblioteket **psutil**.  
Det kan:  
-  Starta övervakning  
-  Lista aktiv status  
-  Skapa larm när gränser passeras  
-  Spara larm i en **JSON-fil** som finns kvar även efter avslut  

---

## Arkitektur

systemmonitor/
├── main.py # Startpunkt, håller ihop programmet
├── menu.py # Meny och input från användaren
├── monitor.py # Funktioner som använder psutil
├── alarms.py # Larmklasser + JSON-hantering
├── utils.py # Hjälpfunktioner
└── alarms.json # Fil där larm sparas

yaml
Kopiera kod

Syftet är att dela upp koden i **moduler**.  
Det gör programmet lättare att förstå, ändra och testa.  

---

## Frågor & Svar (Q&A)

### Kan du förklara vad koden gör?
Den övervakar systemresurser. Programmet mäter CPU, RAM och disk, visar status i konsolen och sparar larm i en JSON-fil när gränser passeras.  

### Varför är arkitekturen uppdelad så här?
För att separera ansvar. Meny för input, monitor för mätning, alarms för logik, utils för stöd.  
👉 Typiskt DevOps tänk: **Separation of concerns**.  

### Varför används psutil?
För att enkelt hämta systemdata i Python:  
```python
import psutil
print(psutil.cpu_percent())
Varför sparas larm i JSON?
För att de ska finnas kvar mellan körningar. JSON är både lättläst för människor och enkelt att hantera i Python:

python
Kopiera kod
import json
with open("alarms.json", "w") as f:
    json.dump({"cpu": "80%"}, f)
Vad händer om psutil inte är installerat?
Programmet kraschar vid import. Lösning: krav i requirements.txt.

Vad händer om alarms.json är korrupt eller saknas?
Då får man fel vid load. En lösning är att skapa en ny tom fil automatiskt.

Hur testades koden?
Genom manuella tester i terminalen:

Startade övervakning

Triggade larm

Kollade att JSON uppdaterades

Vad händer om CPU ligger konstant högt?
Då triggas flera larm. I en vidareutveckling kan man sätta rate limiting (t.ex. ett larm per minut).

Största svagheten i programmet just nu?
Att den inte loggar historisk data. Den visar bara nuvarande status.

Hur kan programmet vidareutvecklas?
Logga historik i fil/databas

Bygga en web-dashboard (t.ex. Flask)

Koppla larm till Slack/Teams

Dockerisera och skicka metrik till Prometheus/Grafana

Kan du visa ett kodexempel på en funktion?
Ja, här är en funktion från monitor.py:

python
Kopiera kod
import psutil

def read_memory():
    return psutil.virtual_memory()

print(read_memory())
Varför är detta relevant i DevOps?
För att övervakning är en kärnuppgift i DevOps.
Den här uppgiften är en förenklad övning som tränar på just grunden: mäta resurser, hantera larm och strukturera kod modulärt.

Krav & Installation
Klona repo

bash
Kopiera kod
git clone https://github.com/[ditt-användarnamn]/systemmonitor.git
cd systemmonitor
Installera beroenden

bash
Kopiera kod
pip install -r requirements.txt
Starta programmet

bash
Kopiera kod
python main.py

