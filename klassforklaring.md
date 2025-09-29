
# Mina klasser i Systemmonitor

Jag har byggt mitt projekt kring några viktiga klasser som tillsammans gör att programmet fungerar smidigt och är lätt att vidareutveckla. Här är min egen förklaring av dem, så som jag själv ser på deras roll och varför jag valt att strukturera det så här:

---

## AlarmManager (Alarms/alarms.py)

AlarmManager är min "larmchef". Den håller reda på alla larm jag skapar, ser till att de sparas till fil och kan laddas in igen när programmet startar. Jag ville ha en central plats för all larmhantering, så att det blir enkelt att lägga till, ta bort och sortera larm. Det gör också att jag kan bygga ut med fler larmtyper i framtiden utan att behöva ändra överallt i koden.

---

## Alarm (Alarms/alarms.py)

Alarm är själva larmet, en enkel klass som bara håller koll på vilken typ av resurs (CPU, minne, disk) och vilken gräns som gäller. Jag gillar att ha tydliga, små klasser för sådant här det gör koden lätt att läsa och testa.

---

## Menu (Menu/menu.py)

Menu är min "programvärd". Den visar alternativen för användaren och ser till att man inte kan göra fel val. Jag har lagt mycket tid på att validera input och göra det tydligt vad som händer, eftersom jag själv tycker det är frustrerande med otydliga menyer i andras program.

---

## Monitor (Monitor/monitor.py)

Monitor är "spanaren" som hämtar aktuell status från datorn: CPU, minne och disk. Jag använder psutil för att få ut dessa värden. Det var en aha-upplevelse att se hur enkelt det går att läsa systemdata i Python!

---

## AlarmType (Alarms/alarms.py)

AlarmType är en liten hjälpare som ser till att larmtyperna är tydliga och konsekventa. Det minskar risken för stavfel och gör det lättare att sortera och visa larm på ett snyggt sätt.

---

## Logger (skapas i Main/main.py)

Logger är min "minnesbok". Allt viktigt som händer både i programmet och under utvecklingen loggas till fil. Det har hjälpt mig att hitta buggar och förstå hur användaren faktiskt använder programmet.

---

Alla dessa klasser har vuxit fram under projektets gång, och jag har försökt göra dem så enkla och tydliga som möjligt. Det har varit lärorikt att se hur mycket lättare det blir att bygga vidare när grunden är stabil och genomtänkt.
