
# Klasser vs Funktioner - Förklaring för Systemmonitor Projektet

## Vad är skillnaden mellan funktioner och klasser?

### Funktioner (som vi använder här)
Tänk på en funktion som en **liten maskin** som gör EN specifik sak:
- Du matar in något (eller inget alls) 
- Den gör sitt jobb
- Du får tillbaka ett resultat

**Exempel från vårt projekt:**
```python
def get_cpu():
    return int(psutil.cpu_percent(interval=1))
```
Denna funktion är som en termometer för din CPU - du "frågar" den och den svarar med procent CPU-användning.

### Klasser (förklaring + exempel)
En klass är som en **ritning** eller **mall** för att skapa många liknande objekt. Lite som en ritning för att bygga hus - från samma ritning kan du bygga många olika hus.

**Exempel på hur vårt projekt SKULLE kunna se ut med klasser:**
```python
class SystemMonitor:
    def __init__(self, name):
        self.name = name
        self.active = False
        self.session_data = []
    
    def get_cpu(self):
        return int(psutil.cpu_percent(interval=1))
    
    def start_monitoring(self):
        self.active = True
        # ... monitoring kod här

# Skapa objekt från klassen
monitor1 = SystemMonitor("Laptop Monitor")  
monitor2 = SystemMonitor("Server Monitor")
```

## Grundläggande Klassförståelse

### Vad är ett objekt?
Ett objekt är som en "påse" som innehåller både:
- **Egenskaper (attributes)**: Vad objektet vet/kommer ihåg
- **Metoder (methods)**: Vad objektet kan göra

**Exempel från verkligheten:**
```python
class Bil:
    def __init__(self, märke, färg):
        self.märke = märke      # Egenskap
        self.färg = färg        # Egenskap  
        self.hastighet = 0      # Egenskap
    
    def accelerera(self):       # Metod
        self.hastighet += 10
    
    def bromsa(self):          # Metod
        self.hastighet -= 10

# Skapa bil-objekt
min_bil = Bil("Volvo", "Röd")
min_bil.accelerera()  # Nu har bilen hastighet 10
```

### Nyckelkoncept att förstå:

**1. Klass = Ritning/Mall**
- Definierar vad objekt av denna typ ska kunna göra
- Beskriver vilka egenskaper objekten ska ha

**2. Objekt = Instans av en klass**  
- Skapad från klassritningen
- Har sina egna unika värden för egenskaperna

**3. self = Referens till objektet själv**
- Används inuti klassen för att komma åt objektets egna egenskaper
- Som att säga "min egen" när man pratar om sig själv

**4. __init__ = Konstruktor**
- Speciell metod som körs när objektet skapas
- Sätter upp objektets grundläggande egenskaper

---

## Varför använde jag funktioner istället för klasser i detta projekt?

### Funktionsbaserat approach passar bättre för detta projekt eftersom:

1. **Enkelhet först** - Som nybörjare är funktioner lättare att förstå och debugga
2. **En funktion = En uppgift** - Mycket tydlig ansvarsfördelning
3. **Mindre kod** - Inga konstruktorer, self-referenser eller objekt-overhead  
4. **Lätt att testa** - Varje funktion kan testas isolerat
5. **Projektets omfattning** - Vi behöver inte flera instanser av samma sak

### När klasser SKULLE vara bättre:

**Om vi hade flera olika typer av monitorer:**
```python
class WindowsMonitor:
    def get_cpu(self):
        # Windows-specifik kod
        return psutil.cpu_percent()
        
class LinuxMonitor:
    def get_cpu(self):
        # Linux-specifik kod  
        return psutil.cpu_percent()

# Skapa rätt typ beroende på OS
if os.name == 'nt':
    monitor = WindowsMonitor()
else:
    monitor = LinuxMonitor()
```

**Om vi ville hantera flera monitorer samtidigt:**
```python
class NetworkMonitor:
    def __init__(self, server_ip):
        self.server_ip = server_ip
        self.connection = None
    
    def connect(self):
        self.connection = connect_to(self.server_ip)

# Övervaka flera servrar
server1 = NetworkMonitor("192.168.1.100")
server2 = NetworkMonitor("192.168.1.101") 
server3 = NetworkMonitor("192.168.1.102")
```

### Mitt projektval: Funktionellt och modulärt

Istället för klasser delade jag upp funktionaliteten i **moduler** (filer):
- `monitor.py` - Systemavläsning
- `alarms.py` - Larmhantering  
- `utils.py` - Hjälpfunktioner
- `logger.py` - Loggning
- `main.py` - Huvudlogik

Detta ger samma **separation of concerns** som klasser, men enklare att förstå!

---

## Så här är mitt projekt organiserat (Verkliga funktioner)

### `monitor.py` - Systemets "sensorer"
```python
def get_cpu():     # Hämta CPU-användning med psutil
def get_ram():     # Hämta RAM-användning i procent  
def get_disk():    # Hämta diskanvändning i procent
```
**Vad gör det:** Som tre olika termometrar - en för CPU, en för RAM, en för disk.  
**Varför funktioner:** Enkla, testbara och återanvändbara systemavläsningar.

### `alarms.py` - Larmhanteringen (Hybrid: Klass + Funktioner)
```python
# OOP-del: Alarm-klass för datastruktur
class Alarm:
    def __init__(self, alarm_type, threshold):
        self.type = alarm_type
        self.threshold = threshold
    
    def is_triggered(self, value):
        return value >= self.threshold
    
    def __str__(self):
        return f"{self.type} alarm {self.threshold}%"

# Funktionell del: Larmhantering
def create_new_alarm():        # Skapa nytt larm via användarinput
def show_all_alarms():         # Visa alla sparade larm
def edit_delete_alarms():      # Redigera eller ta bort befintliga larm
def save_alarms():             # Spara larm till JSON-fil
def load_alarms():             # Ladda larm från JSON-fil
def check_alarms(cpu, ram, disk): # Utvärdera om larm ska triggas
```
**Vad gör det:** Hybrid-approach - `Alarm`-klass för datarepresentation, funktioner för operations.  
**Varför hybrid:** Klassen representerar naturligt ett "larm" som koncept, funktionerna hanterar operations.

### `utils.py` - Hjälpfunktioner & Filhantering
```python
def save_session_data(data):   # Spara övervakningsdata till JSON
def get_last_session_file():   # Hitta senaste session-fil
def pretty_print_status():     # Formatera systemstatus elegant  
def clear_screen():            # Rensa terminalskärm
```
**Vad gör det:** Filoperationer, UI-hjälp och datahantering.  
**Varför funktioner:** Återanvändbara verktyg utan objekts-overhead.

### `logger.py` - Händelseloggning
```python
def write_log(message):        # Skriv händelser till log-fil med timestamp
```
**Vad gör det:** Enkel men effektiv loggning av alla programhändelser.  
**Varför funktioner:** Loggning behöver bara EN operation - skriv meddelande.

### `main.py` - Huvudprogrammet & Orchestration
```python
def start_monitoring():        # Kör 10-iterations övervakningsloop
def show_status():             # Visa aktuell systemstatus  
def show_last_session():       # Visa data från senaste session
def simple_monitoring():       # Enklare 5-readings övervakningsläge
def show_menu():               # Visa huvudmeny
def main():                    # Huvudloop med felhantering
```
**Vad gör det:** Orkestrerar alla moduler och hanterar användarinteraktion.  
**Varför funktioner:** Tydlig separation mellan olika användaroperationer.

---

## Min Verkliga Användning av Klasser i Projektet

### Alarm-klassen: Smart OOP-användning

Jag valde att använda en klass för `Alarm` eftersom det representerar ett naturligt "objekt" med egenskaper och beteenden:

```python
class Alarm:
    """Representerar ett enskilt larm med typ och tröskelvärde."""
    def __init__(self, alarm_type, threshold):
        self.type = alarm_type          # Vilken typ av larm (CPU/RAM/DISK)
        self.threshold = threshold      # Vid vilken procent ska larmet triggas
    
    def is_triggered(self, value):
        """Returnerar True om värdet överskrider tröskeln."""
        return value >= self.threshold
    
    def __str__(self):
        return f"{self.type} alarm {self.threshold}%"
```

### Så använder jag klassen i praktiken:

**1. Skapa alarm-objekt:**
```python
# I create_new_alarm() funktionen
new_alarm = Alarm("CPU", 80)
alarms.append(new_alarm.__dict__)  # Spara som dict för JSON
```

**2. Kontrollera om alarm triggas:**
```python
# I check_alarms() funktionen  
for alarm_data in alarms:
    alarm = Alarm(alarm_data["type"], alarm_data["threshold"])
    if alarm.is_triggered(cpu_value):
        print(f"ALARM: {alarm}")  # Använder __str__ metoden
```

### Varför denna hybrid-approach är smart:

✅ **Naturlig datarepresentation** - Ett "larm" är intuitivt ett objekt  
✅ **Inkapsling av logik** - `is_triggered()` metoden tillhör larmet  
✅ **Enkel att förstå** - Tydligt vad klassen representerar  
✅ **JSON-kompatibel** - `__dict__` gör det enkelt att spara  
✅ **Minimal komplexitet** - Endast en liten, fokuserad klass  

### Detta visar att jag förstår:

- **När klasser är lämpliga** - För naturliga objekt med egenskaper och beteenden
- **Hur man kombinerar paradigm** - Funktioner för operations, klasser för data
- **Praktisk OOP** - Använd klasser när de tillför värde, inte för sakens skull

---

## Alternativ Klassbaserad Design (Teoretisk)

### Hur projektet SKULLE kunna struktureras med klasser:

```python
# Teoretisk klassbaserad approach
class SystemMonitor:
    def __init__(self):
        self.active = False
        self.session_data = []
        self.current_cpu = 0
        self.current_ram = 0  
        self.current_disk = 0
        
    def get_system_stats(self):
        self.current_cpu = psutil.cpu_percent()
        self.current_ram = psutil.virtual_memory().percent
        self.current_disk = psutil.disk_usage('/').percent
        
    def start_monitoring(self):
        self.active = True
        for i in range(10):
            self.get_system_stats()
            # ... resten av logiken

class AlarmManager:
    def __init__(self):
        self.alarms = []
        
    def add_alarm(self, alarm_type, threshold):
        self.alarms.append({"type": alarm_type, "threshold": threshold})
        
    def check_alarms(self, cpu, ram, disk):
        # ... larmkontroll logik

# Användning
monitor = SystemMonitor()
alarm_manager = AlarmManager()
monitor.start_monitoring()
```

### Varför jag INTE valde detta:

1. **Mer komplex** - Kräver förståelse av self, konstruktorer, objektreferenser
2. **Overkill för projektets scope** - Vi behöver inte flera instanser
3. **Svårare att debugga** - Objekttillstånd kan vara svårt att spåra
4. **Längre utvecklingstid** - Mer boilerplate-kod att skriva och underhålla

### När klassbaserad design SKULLE vara bättre:

```python
# Om vi övervakade flera system samtidigt
class RemoteSystemMonitor:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None
        self.last_update = None
    
    def connect(self):
        self.connection = establish_connection(self.hostname, self.port)
    
    def get_remote_stats(self):
        return self.connection.fetch_system_data()

# Skapa flera monitorer
servers = [
    RemoteSystemMonitor("web-server-1", 8080),
    RemoteSystemMonitor("db-server-1", 3306), 
    RemoteSystemMonitor("cache-server-1", 6379)
]

for server in servers:
    server.connect()
    stats = server.get_remote_stats()
```

**I detta fall skulle klasser ge:**
- **Inkapsling** - Varje server har sina egna anslutningsdata
- **Tillståndshantering** - Varje objekt kommer ihåg sin status
- **Skalbarhet** - Lätt att lägga till fler servrar

---

## Så här tänker du som programmerare

### 1. **Bryt ner problem i små delar**
Istället för att tänka "jag ska bygga en systemmonitor" (skrämmande stort!), tänk:
- "Jag behöver läsa CPU-värden" → `cpu()` funktion
- "Jag behöver spara data" → `save()` funktion  
- "Jag behöver visa en meny" → `main()` funktion

### 2. **En funktion = Ett ansvar**
```python
# BRA: Gör EN sak
def cpu():
    return psutil.cpu_percent(interval=1)

# DÅLIGT: Gör för många saker
def cpu_and_save_and_show():
    cpu = psutil.cpu_percent()
    save_to_file(cpu)
    print(cpu)
    return cpu
```

### 3. **Testbarhet**
Med funktioner kan du enkelt testa varje del:
```python
# Testa att CPU-funktionen fungerar
print(cpu())  # Borde visa ett tal mellan 0-100
```

---

## Tips för dig som nybörjare

### Börja alltid med funktioner!
- De är lättare att förstå
- Du lär dig grunderna först  
- Du kan alltid bygga om till klasser senare

### Namnge funktioner tydligt
```python
# BRA namn (du förstår direkt vad den gör)
def get_cpu_percentage():

# DÅLIGT namn (vad gör "process"?)  
def process():
```

### Håll funktioner korta
Om en funktion är längre än din skärm, dela upp den i mindre funktioner!

---

## Djupare Klassförståelse - Viktiga Koncept

### Arv (Inheritance) - "Ärva" egenskaper från andra klasser

```python
# Baseklass med gemensam funktionalitet
class BaseMonitor:
    def __init__(self, name):
        self.name = name
        self.active = False
    
    def start(self):
        self.active = True
        print(f"{self.name} started")
    
    def stop(self):
        self.active = False
        print(f"{self.name} stopped")

# Specialiserade klasser som "ärver" från BaseMonitor
class CPUMonitor(BaseMonitor):
    def __init__(self, name, threshold):
        super().__init__(name)  # Anropa föräldraklassens konstruktor
        self.threshold = threshold
    
    def check_cpu(self):
        cpu_usage = psutil.cpu_percent()
        if cpu_usage > self.threshold:
            return f"CPU Alert: {cpu_usage}% > {self.threshold}%"
        return "CPU OK"

class MemoryMonitor(BaseMonitor):
    def __init__(self, name, max_memory):
        super().__init__(name)
        self.max_memory = max_memory
    
    def check_memory(self):
        mem = psutil.virtual_memory()
        if mem.used > self.max_memory:
            return f"Memory Alert: {mem.used} > {self.max_memory}"
        return "Memory OK"

# Användning
cpu_monitor = CPUMonitor("CPU Watcher", 80)
mem_monitor = MemoryMonitor("Memory Watcher", 8000000000)

cpu_monitor.start()  # Ärvd från BaseMonitor
result = cpu_monitor.check_cpu()  # Egen metod
```

### Inkapsling (Encapsulation) - Gömma intern data

```python
class SecureAlarmSystem:
    def __init__(self):
        self.__secret_code = "1234"  # Privat attribut (dubbel underscore)
        self._internal_alarms = []    # "Skyddad" attribut (enkel underscore)
        self.public_status = "OK"    # Publik attribut
    
    def authenticate(self, code):
        return code == self.__secret_code
    
    def add_alarm(self, alarm, user_code):
        if self.authenticate(user_code):
            self._internal_alarms.append(alarm)
            return "Alarm added"
        return "Access denied"
    
    def get_alarm_count(self):
        return len(self._internal_alarms)  # Kontrollerad åtkomst till intern data

# Användning
alarm_system = SecureAlarmSystem()
# alarm_system.__secret_code  # FEL! Går ej att komma åt direkt
alarm_system.add_alarm("High CPU", "1234")  # OK med rätt kod
```

### Polymorfism - Samma interface, olika implementering

```python
class NotificationSender:
    def send(self, message):
        raise NotImplementedError("Subclass must implement send()")

class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSSender(NotificationSender):
    def send(self, message):
        print(f"SMS sent: {message}")

class SlackSender(NotificationSender):
    def send(self, message):
        print(f"Slack message: {message}")

# Polymorfism i action - samma metod, olika beteende
def notify_admin(sender, message):
    sender.send(message)  # Vet inte vilken typ, men alla har send()

# Fungerar med alla typer
notifiers = [
    EmailSender(),
    SMSSender(), 
    SlackSender()
]

for notifier in notifiers:
    notify_admin(notifier, "System Alert!")
```

### Komposition - Bygga komplexa objekt från enklare

```python
class Sensor:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit
        self.value = 0
    
    def read(self):
        # Simulera sensoravläsning
        import random
        self.value = random.randint(0, 100)
        return self.value

class Dashboard:
    def __init__(self):
        # Komposition - Dashboard "har" sensorer
        self.cpu_sensor = Sensor("CPU", "%")
        self.ram_sensor = Sensor("RAM", "%") 
        self.disk_sensor = Sensor("Disk", "%")
        self.sensors = [self.cpu_sensor, self.ram_sensor, self.disk_sensor]
    
    def update_all(self):
        results = {}
        for sensor in self.sensors:
            results[sensor.name] = f"{sensor.read()}{sensor.unit}"
        return results
    
    def get_critical_sensors(self, threshold=80):
        critical = []
        for sensor in self.sensors:
            if sensor.value > threshold:
                critical.append(f"{sensor.name}: {sensor.value}{sensor.unit}")
        return critical

# Användning
dashboard = Dashboard()
data = dashboard.update_all()
alerts = dashboard.get_critical_sensors(75)
```

## Varför valde jag funktioner för DETTA projekt?

### Funktionella fördelar för vårt projekt:

1. **Enkelhet** - Inga objekt att hålla reda på
2. **Testbarhet** - Varje funktion kan testas isolerat
3. **Moduläritet** - Tydlig separation mellan filer/moduler  
4. **Prestanda** - Ingen objektskapande overhead
5. **Läsbarhet** - Linjär kodflöde, lätt att följa

### När klasser blir värdefulla:

1. **Flera instanser behövs** - Övervaka flera servrar samtidigt
2. **Komplext tillstånd** - Objekt som måste komma ihåg mycket data
3. **Hierarkier** - Olika typer med gemensam funktionalitet
4. **Inkapsling krävs** - Skydda intern data från felaktig användning
5. **Polymorfism behövs** - Samma interface, olika implementeringar

---

## Sammanfattning - Funktioner vs Klasser i mitt projekt

### Funktioner är perfekta för detta projekt eftersom:

**Projektkaraktär:**
- **Single-purpose application** - Övervakar ETT system åt gången
- **Begränsad omfattning** - Tydligt definierat scope och funktionalitet  
- **Enkel dataflöde** - Linjär bearbetning utan komplex tillståndshantering
- **Stateless operations** - De flesta operationer behöver inte komma ihåg tidigare tillstånd

**Utvecklingsfördelar:**
- **Snabb prototyping** - Funktioner är snabbare att skriva och testa
- **Lättare debugging** - Inga objektreferenser eller tillstånd att spåra
- **Tydlig modulär struktur** - Varje fil har tydligt ansvar
- **Minimal boilerplate** - Ingen self, konstruktorer eller klasshiearkier

**Kodkvalitet:**
- **Hög testbarhet** - Varje funktion kan unit-testas isolerat
- **God läsbarhet** - Koden flödar logiskt uppifrån och ner
- **Låg komplexitet** - Inga abstraktionslager att navigera
- **Enkel underhållbarhet** - Lätt att hitta och ändra specifik funktionalitet

### Klasser skulle vara bättre om projektet hade:

**Skalbarhetsbehov:**
```python
# Övervaka flera system samtidigt
monitors = [
    SystemMonitor("Server-1", "192.168.1.100"),
    SystemMonitor("Server-2", "192.168.1.101"), 
    SystemMonitor("Database", "192.168.1.200")
]
```

**Komplex tillståndshantering:**
```python
# Objekt som måste komma ihåg historik
class TrendAnalyzer:
    def __init__(self):
        self.cpu_history = []
        self.prediction_model = None
        self.last_analysis = None
```

**Olika beteenden för samma koncept:**
```python
# Polymorfism för olika alarmtyper  
class EmailAlarm(BaseAlarm):
    def trigger(self):
        send_email(self.message)

class SlackAlarm(BaseAlarm): 
    def trigger(self):
        send_slack(self.message)
```

**Inkapsling av känslig data:**
```python
# Skydda konfiguration och credentials
class SecureMonitor:
    def __init__(self):
        self.__api_key = load_secret_key()
        self.__config = load_secure_config()
```

### Min Design Decision Matrix

| Faktor | Funktioner | Klasser | Mitt Val |
|--------|------------|---------|----------|
| **Komplexitet** | Låg | Hög | ✅ Funktioner |
| **Utvecklingshastighet** | Snabb | Långsammare | ✅ Funktioner |
| **Skalbarhet** | Begränsad | Hög | ✅ Funktioner (räcker) |
| **Underhållbarhet** | Hög (för små projekt) | Hög (för stora projekt) | ✅ Funktioner |
| **Testbarhet** | Mycket hög | Hög | ✅ Funktioner |
| **Återanvändbarhet** | Modulnivå | Objektnivå | ✅ Funktioner (moduler) |
| **Prestanda** | Optimal | Bra | ✅ Funktioner |

### Vad jag har lärt mig om OOP

**Förståelse av när att INTE använda klasser är lika viktigt som att förstå när man ska använda dem.**

**Fyra pilarer av OOP och när de är relevanta:**

1. **Inkapsling** - Behövdes inte (ingen känslig data att skydda)
2. **Arv** - Behövdes inte (inga gemensamma beteenden att dela)  
3. **Polymorfism** - Behövdes inte (ingen variation i implementations)
4. **Abstraktion** - Uppnått genom modulär funktionsdesign

**Min arkitektoniska strategi:**
- **Separation of Concerns** via moduler istället för klasser
- **Single Responsibility Principle** genom funktionsdesign
- **DRY (Don't Repeat Yourself)** genom återanvändbara utility-funktioner
- **KISS (Keep It Simple, Stupid)** genom att undvika onödig komplexitet

### Detta visar att jag förstår:

✅ **OOP-principer** - Vet vad klasser, objekt, arv och polymorfism är  
✅ **Design patterns** - Förstår när olika mönster är lämpliga  
✅ **Arkitektoniska beslut** - Kan motivera teknikval baserat på projektbehov  
✅ **Pragmatisk programmering** - Väljer rätt verktyg för jobbet  
✅ **Code quality principles** - Prioriterar läsbarhet, testbarhet och underhållbarhet



---

