# Klasser i Systemmonitor 

Här kommer en enkel förklaring av de viktigaste klasserna i mitt projekt!

---

## 1. AlarmManager (Alarms/alarms.py)

**Vad gör den?**
- Tänk dig en låda där vi kan lägga olika larm.
- AlarmManager hjälper oss att lägga till, ta bort och spara larm i lådan.
- Den kan också läsa in gamla larm från en lista (fil) när vi startar programmet.

**Varför behövs den?**
- Så vi kan hålla koll på alla larm och inte glömma bort dem!

---

## 2. Alarm (Alarms/alarms.py)

**Vad gör den?**
- Ett larm är som en liten vakt som säger till om något blir för mycket.
- Till exempel: "Om CPU blir över 80%, ropa högt!"
- Varje larm har en typ (CPU, minne, disk) och en gräns (t.ex. 80%).

**Varför behövs den?**
- Så vi vet exakt vad vi ska vakta på!

---

## 3. Menu (Menu/menu.py)

**Vad gör den?**
- Menu är som en snäll vuxen som frågar: "Vad vill du göra nu?"
- Den visar olika val och hjälper dig att välja rätt sak.
- Den ser till att du inte gör något tokigt (t.ex. skriver fel).

**Varför behövs den?**
- Så det blir lätt att styra programmet och välja vad man vill göra!

---

## 4. Monitor (Monitor/monitor.py)

**Vad gör den?**
- Monitor är som en superhjälte som kan titta på datorns hjärna (CPU), minne och hårddisk.
- Den berättar hur mycket som används just nu.

**Varför behövs den?**
- Så vi vet om datorn mår bra eller om den jobbar för hårt!

---

## 5. AlarmType (Alarms/alarms.py)

**Vad gör den?**
- AlarmType är som etiketter på larmen: "Det här är ett CPU-larm!"
- Hjälper oss att hålla ordning på olika sorters larm.

**Varför behövs den?**
- Så vi inte blandar ihop larmen!

---

## 6. Logger (skapas i Main/main.py)

**Vad gör den?**
- Logger är som en dagbok som skriver ner allt viktigt som händer.
- Den sparar vad vi gör och när vi gör det.

**Varför behövs den?**
- Så vi kan titta tillbaka och se vad som har hänt!

---

Alla dessa klasser jobbar tillsammans så att vi kan hålla koll på datorn, sätta larm och se vad som händer – precis som ett riktigt övervakningsteam!
