
---

## 🤔 Vad är skillnaden mellan funktioner och klasser?

### Funktioner (som vi använder här)
Tänk på en funktion som en **liten maskin** som gör EN specifik sak:
- Du matar in något (eller inget alls)
- Den gör sitt jobb
- Du får tillbaka ett resultat

**Exempel från vårt projekt:**
```python
def cpu():
    return psutil.cpu_percent(interval=1)
```
Denna funktion är som en termometer för din CPU - du "frågar" den och den svarar med temperaturen (procent CPU-användning).

### Klasser (som vi INTE använder här)
En klass är som en **ritning** eller **mall** för att skapa många liknande objekt. Lite som en ritning för att bygga hus - från samma ritning kan du bygga många olika hus.

---

## 🏗️ Varför använde jag funktioner istället för klasser?

Som nybörjare är det MYCKET lättare att förstå funktioner eftersom:

1. **En funktion = En uppgift** (mycket tydligt!)
2. **Du kan läsa koden uppifrån och ner** (logisk ordning)
3. **Inga konstiga koncept** som "konstruktorer" eller "arv" att förvirra dig
4. **Snabbare att skriva och testa**

---

## 📁 Så här är mitt projekt organiserat

### `monitor.py` - Systemets "sensorer"
```python
def cpu():     # Hämta CPU-användning
def mem():     # Hämta minnesanvändning  
def disk():    # Hämta diskanvändning
```
**Vad gör det:** Som tre olika termometrar - en för CPU, en för minne, en för disk.  
**Varför är det bra:** Du förstår direkt vad varje funktion gör genom namnet!

### `alarms.py` - Larmhanteringen
```python
def load():                    # Ladda sparade larm från fil
def save(alarms):             # Spara larm till fil  
def create(metric, threshold): # Skapa ett nytt larm
def delete(id):               # Ta bort ett larm
def evaluate(cpu, mem, disk): # Kolla om något larm ska triggas
```
**Vad gör det:** Som en larmklocka som du kan ställa olika tider på.  
**Varför är det bra:** Varje funktion gör EN sak - lätt att förstå och testa!

### `utils.py` - Hjälpfunktioner
```python
def gb(bytes):        # Konvertera bytes till gigabyte
def press():          # Vänta på att användaren trycker Enter
def beep():           # Spela ett ljud
```
**Vad gör det:** Som en verktygslåda full med små användbara verktyg.  
**Varför är det bra:** Istället för att upprepa samma kod överallt har vi små hjälpare!

### `main.py` - Huvudprogrammet
```python
def start_overvakning():     # Starta övervakning
def create_alarm():          # Meny för att skapa larm
def show_alarms():           # Visa alla larm
def main():                  # Huvudmenyn
```
**Vad gör det:** Som en dirigent som styr hela orkestern.  
**Varför är det bra:** Allt är uppdelat i tydliga, testbara bitar!

---

## 🧠 Så här tänker du som programmerare

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

## 🚀 Tips för dig som nybörjare

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

## 🎯 När skulle vi använda klasser istället?

Du skulle använda klasser om du ville ha flera "systemmonitorer" som fungerar olika:

```python
# Detta behöver vi INTE för vårt projekt
class WindowsMonitor:
    def cpu(self): # Kod för Windows
        
class LinuxMonitor:  
    def cpu(self): # Kod för Linux
        
class MacMonitor:
    def cpu(self): # Kod för Mac
```

Men eftersom vi bara övervakar ETT system åt gången räcker funktioner gott och väl!

---

## 💡 Sammanfattning för dig som student

**Funktioner är perfekta när du:**
- ✅ Är ny på programmering
- ✅ Vill lösa ett specifikt problem  
- ✅ Behöver kod som är lätt att förstå och testa
- ✅ Arbetar med ett mindre projekt (som detta)

**Klasser är bättre när du:**
- 🔄 Behöver många liknande objekt
- 🏭 Bygger stora, komplexa system
- 👥 Arbetar i stora team
- 🔄 Behöver "ärva" egenskaper mellan olika typer

**För din första DevOps-resa: Stick med funktioner! Du har redan tillräckligt att lära dig med Docker, Git, terminaler och deployment. Lär dig gå innan du springer! 🏃‍♂️**

---

