## Systemmonitor – Projektstruktur & Arkitektur

```text
systemmonitor/
│
├── main.py        # startpunkt, anropar menyn
├── menu.py        # menylogik, input-hantering
├── monitor.py     # CPU/RAM/Disk-funktioner
├── alarms.py      # Alarm-klass + larmhantering
└── requirements.txt (psutil)
```

---

### Projektbeskrivning (på svenska)

Detta är ett övningsprojekt för att lära mig grunderna i Python och systemövervakning.

**Syfte:**
- Bygga en enkel systemmonitor som kan visa CPU-, RAM- och diskanvändning.
- Implementera larmfunktioner för att varna vid höga värden.
- Träna på att strukturera kod och använda externa bibliotek (psutil).

**Arkitektur:**
- `main.py` – Startpunkt, anropar menyn.
- `menu.py` – Hanterar menyval och användarinput.
- `monitor.py` – Funktioner för att läsa av systemresurser.
- `alarms.py` – Klass och logik för larm.
- `requirements.txt` – Lista över beroenden (psutil).

---

> "No man has the right to be an amateur in the matter of physical training. It is a
shame for a man to grow old without seeing the beauty and strenght of which his body is capable."

- Sokrates
