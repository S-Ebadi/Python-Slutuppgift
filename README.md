# Observera

Detta README och projektstruktur beskriver det tänkta slutmålet för systemmonitor-applikationen. Nuvarande implementation och faktisk kunskapsnivå framgår av loggfilen som förs under utvecklingen. Funktionalitet, struktur och kodstil är under pågående arbete och uppdateras löpande. Originalplanen och nuvarande utseende bibehålls, men utgå från loggfilen för att se vad som faktiskt är genomfört och vilka insikter som vunnits hittills.


# Systemmonitor

Systemmonitor är en konsolapplikation skriven i Python för övervakning av CPU-, minnes- och diskanvändning. Programmet erbjuder larmfunktioner, loggning av händelser och en användarvänlig meny för interaktion.

## Innehållsförteckning

- [Projektstruktur](#projektstruktur)
- [Installation](#installation)
- [Användning](#användning)
- [Loggning och larmhantering](#loggning-och-larmhantering)
- [Kända begränsningar](#kända-begränsningar)

## Projektstruktur

```text
Slutuppgift/
│
├── Main/
│   └── main.py         # Startpunkt för programmet
├── Menu/
│   └── menu.py         # Menylogik och användarinteraktion
├── Monitor/
│   └── monitor.py      # Funktioner för systemövervakning
├── Alarms/
│   └── alarms.py       # Larmklasser och larmhantering
├── Storage/
│   └── __init__.py     # (Reserv för framtida lagring)
├── logs/               # Loggfiler skapas här
├── alarms.json         # Persistenta larmdata
├── requirements.txt    # Beroenden (psutil)
└── README.md           # Denna fil
```

## Installation

1. Klona detta repository:
	```bash
	git clone <repo-url>
	cd Slutuppgift/Slutuppgift
	```
2. Skapa och aktivera ett virtuellt Python-miljö (valfritt men rekommenderas):
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```
3. Installera beroenden:
	```bash
	pip install -r requirements.txt
	```

## Användning

Starta programmet från projektroten:

```bash
python Main/main.py
```

Vid start möts du av en meny med följande alternativ:

1. Starta övervakning
2. Lista aktiv övervakning
3. Skapa larm
4. Visa larm
5. Starta övervakningsläge
6. Ta bort larm
7. Avsluta

Följ instruktionerna i konsolen för att navigera mellan alternativen. Alla inmatningar valideras och felaktig input hanteras.

## Loggning och larmhantering

- Alla händelser loggas automatiskt till en fil i `logs/`-mappen. Loggfilen namnges med datum och tid för programstart.
- Alla larm sparas automatiskt i `alarms.json` och laddas vid programstart.
- Du kan skapa flera larm av samma typ och ta bort larm via menyn.
- Endast det närmaste larmet av en viss typ aktiveras om flera trösklar överskrids.

## Kända begränsningar

- Programmet kräver Python 3.8 eller senare.
- Testad på macOS och Windows.
- Kräver rättigheter att läsa systeminformation (psutil).
- `Laborationer/`-mappen används endast för utveckling och ska tas bort inför inlämning.

---

## Reflektion och lärdomar

Under arbetet med denna slutuppgift har jag lärt mig:

- Hur man strukturerar ett större Python-projekt med flera moduler och klasser.
- Versionshantering med git och vikten av tydlig projektstruktur.
- Hur man använder externa bibliotek som psutil för att läsa systemresurser.
- Betydelsen av loggning, både för utvecklingsprocessen och för själva applikationen.
- Att validera användarinput och hantera fel på ett robust sätt.
- Hur man iterativt förbättrar kod och dokumentation utifrån logg och feedback.

Min progression och faktiska kunskapsnivå framgår tydligt av loggfilen (`Loggning(Delavstämning)/loggin.md`). Där dokumenteras dag för dag vad som genomförts, vilka problem som uppstått och hur de lösts. Klassförklaringar på enkel nivå finns i `klassforklaring.md`.

---

> "No man has the right to be an amateur in the matter of physical training. It is a shame for a man to grow old without seeing the beauty and strength of which his body is capable."

— Sokrates
