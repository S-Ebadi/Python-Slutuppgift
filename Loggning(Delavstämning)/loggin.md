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
- Började bygga menyn för att starta/stoppa övervakning.

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

## Nästa steg - 30 september
- Implementera färdigt larmflöde för minne och disk.
- Bygga färdiga klasser enligt OOP-principer.
- Lägga till testfall och förbereda slutgiltig dokumentation.