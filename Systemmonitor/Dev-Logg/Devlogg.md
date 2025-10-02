# Slutuppgift (Systemmonitor i Python) - Logg

Syfte: Dokumentera dagliga aktiviteter, tekniska beslut och lärdomar under arbetet med slutuppgiften.  
Period: 22 september – pågående

---

## 22 september
- Startade skiss på arkitektur: definierade moduler `main.py`, `menu.py`, `monitor.py`, `alarms.py`.
- Skapade Git-repo och grundmappstruktur.
- Fördjupade förståelse för VS Code och Git, inklusive init, commit och push.

**Lärdomar:**  
- Första version av projektplan.  
- Git-arbetsflöde (init–commit–push) nu självklarhet.

---

## 23 september
- Städade mappar och filer för bättre översikt och framtida CI/CD-stöd.
- Förberedde frågor till handledare kring loggkrav:  
  - Om logg ska omfatta endast utvecklingsprocess eller även användarloggning i appen.
- Införde daglig aktivitetslogg för att följa DevOps-principen “mät och förbättra”.

**Lärdomar:**  
- Struktur och versionskontroll är en central del av DevOps, inte bara kod.

---

## 25 september
- Installerade och testade `psutil` för systemresursövervakning.  
- Verifierade `psutil.cpu_percent()` och andra metoder för minne och disk.
- Började bygga menyn för att starta och stoppa övervakningsläge.

**Lärdomar:**  
- Förståelse för hur Python kan interagera direkt med OS-resurser.  
- Grund för CPU-, minnes- och disklarm.

---

## 26 september
- Sidoprojekt: rensade och konfigurerade terminalprompt för renare arbetsmiljö (endast `$`).  
- Dokumenterade processen i en separat README och publicerade som eget Git-repo.
- Förbättrade arbetsflöde i terminalen, snabbare navigering mellan projekt.

**Lärdomar:**  
- Fördjupad kunskap om zsh och terminalkonfiguration.  
- Effektivare utvecklingsmiljö ger direkt bättre fokus i huvudprojektet.

---

## 27 september
- Införde grundläggande felhantering i menyn (validering av menyval, hantering av ogiltig input).
- Började skriva **README-draft** med projektbeskrivning, arkitekturöversikt och körinstruktioner.
- Påbörjade diskussion kring användarloggning för framtida utveckling.

**Lärdomar:**  
- Välstrukturerad README är avgörande för samarbete och framtida underhåll.

---

## 28 september
- Testade larmfunktioner för höga CPU-värden med `psutil` och implementerade grund för notifieringar.  
- Planerade nästa steg: refaktorering till objektorienterad struktur (klasser för monitorering och larm).

**Lärdomar:**  
- Bekräftade värdet av modulär arkitektur: enklare att utöka med nya resurstyper (ex. nätverk).

---

## 29 september
- Gått igenom och dubbelkollat all kodstruktur och dokumentation för att säkerställa att allt hänger ihop logiskt.
- Skapat README-filer för samtliga mappar för att tydliggöra syfte och ansvar i varje del av projektet.
- Reflekterat över vikten av att förstå syftet med varje klass och funktion innan implementation märker att det ger färre buggar och bättre kod.
- Läst på mer om loggning och best practices för dokumentation, och försökt applicera det i projektet.
- Upptäckt att det är lätt att missa detaljer om man stressar och har därför börjat arbeta mer metodiskt och stämmer av mot krav och tidigare loggar.

**Lärdomar:**  
- Min förståelse för helheten har ökat, men jag inser också att det krävs fortsatt noggrannhet och att jag behöver dubbelkolla både teori och praktik.
- Det känns bra att se progression, men jag är ödmjuk inför att det är mycket kvar att lära och att det är viktigt att ta ett steg i taget.

---

## 30 september
- Kände viss oro kring uppgiften och behovet att förstå helheten bättre.  
- Gjorde därför en “back to basics”-övning: kartlade flödet steg för steg (“meny → monitor → alarms”), vilket gav bättre grepp om logiken.  
- Förberedde mig inför presentation genom att öva på att förklara logiken muntligt, inte bara visa kod.  

**Lärdomar:**  
- En tydlig mental modell gör det lättare att förklara för andra.  
- Förståelsen blir starkare när jag inte bara kör kod, utan även förklarar lösningen högt.

---

## 1 oktober
- Arbetade vidare med menyn och anpassade den strikt efter instruktionen (fem huvudval).  
- Implementerade tydligare hantering för att skapa, visa och redigera larm.  
- Justerade koden så att övervakning alltid är ett aktivt övervakningsläge, inte en snapshot.  
- Reflekterade över hur små förändringar i menyer och logik gör programmet mer professionellt.  

**Lärdomar:**  
- Att läsa och följa instruktionerna ordagrant är avgörande.  
- Minimalism i menystrukturen ger ett mer robust och begripligt system.  

---

## 2 oktober
- Införde möjlighet att avsluta övervakningsläge med Enter istället för Ctrl+C, vilket gör det mer användarvänligt.  
- Lade till menyval för att visa resultat från senaste övervakningen, inklusive summering av mätpunkter och larm.  
- Testade hela flödet: starta övervakning, skapa larm, trigga larm, avsluta, visa resultat.  
- Skiftade fokus från ren kodning till att förbereda presentation och dokumentation.  

**Lärdomar:**  
- Att visa upp “senaste session” räcker för att tydliggöra förståelse för krav och logik.  
- Presentationen behöver kombinera teknik (kod och funktion) med process (lärande och utveckling).  

---

## 3 oktober (planerat)
- Gå igenom hela koden igen och säkerställa att varje menyval följer instruktionerna ordagrant.  
- Testa olika typer av larm (CPU, minne, disk) för att verifiera att alla fungerar korrekt.  
- Förbereda några vanliga frågor och svar till presentationen, exempelvis:  
  - Varför är programmet uppdelat i flera filer?  
  - Hur fungerar larmhanteringen i praktiken?  

**Agenda:**  
- Fokus på att befästa förståelse snarare än att skriva ny kod.  
- Träna på muntlig förklaring av koden.

---

## 4 oktober (planerat)
- Skriva en enkel checklista för att demonstrera programmet live: vilka steg som ska visas och i vilken ordning.  
- Göra en torrkörning där jag låtsas presentera för en publik.  
- Förtydliga README-filen med körinstruktioner och exempelutdata.  

**Agenda:**  
- Skifta fokus från kod till presentation.  
- Säkerställa att all dokumentation är tillräckligt tydlig för någon annan att förstå projektet.

---

## 5 oktober (planerat)
- Repetera teorin bakom Python-funktioner, klasser och JSON, för att kunna svara på frågor utan att bara hänvisa till koden.  
- Lägga till första utkast till en metareflektion för nästa period (3–5 okt).  
- Stämma av mot kursens kravlista och bocka av punkter som är uppfyllda.  

**Agenda:**  
- Säkerställa att både teori och praktik sitter.  
- Skapa underlag för nästa veckas arbete med presentation och finputs.


## Metareflektion (22 sep – 2 okt)
Den här perioden började med att bygga struktur och grundläggande kod, och har utvecklats till att handla om att förstå helheten och förbereda presentationen. Från att initialt känna viss osäkerhet över komplexiteten, har jag genom dagliga loggar och metodiskt arbete lyckats bryta ner problemet i hanterbara steg. Jag ser tydligt hur både tekniska färdigheter (psutil, menyer, JSON-lagring) och arbetsmetod (struktur, reflektion, dokumentation) har stärkts. Viktigast av allt: jag känner att jag kan förklara mitt system på ett enkelt och trovärdigt sätt, vilket är målet inför inlämning och redovisning.
