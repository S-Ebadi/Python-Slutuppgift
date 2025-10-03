# 📝 CHEATSHEET – Systemmonitor

Denna guide samlar alla nödvändiga terminal-, Python- och Git-kommandon för att navigera, köra och underhålla **Systemmonitor-projektet**.  
Syftet är att snabbt kunna hitta rätt kommando inför utveckling, testning och presentation.

---

## 📂 Navigering i terminalen

pwd               # Visa nuvarande mapp (print working directory)  
ls                # Lista filer och mappar i nuvarande mapp  
cd ..             # Gå upp en nivå  
cd systemmonitor  # Gå in i mappen "systemmonitor"  

---

## 🚀 Köra projektet

python3 main.py              # Starta systemmonitor-programmet (om du står i systemmonitor/)  
python3 systemmonitor/main.py # Starta om du kör från roten av projektet  

---

## 📑 Kolla filer

ls systemmonitor            # Lista alla filer i mappen systemmonitor  
cat systemmonitor/main.py   # Visa innehållet i main.py i terminalen  
less systemmonitor/main.py  # Bläddra i filen (tryck q för att avsluta)  

---

## 🛠️ Redigera filer

code systemmonitor/main.py  # Öppna main.py i VS Code (om code är installerat)  
code .                      # Öppna hela projektet i VS Code  

---

## 📦 Python-miljö och beroenden

pip install -r requirements.txt   # Installera beroenden  
pip list                          # Visa installerade paket  

---

## 📜 JSON & Loggar

ls systemmonitor/Storage                  # Lista sessions- och loggfiler  
cat systemmonitor/Storage/alarms.json     # Se sparade larm  
cat systemmonitor/Storage/session-*.json  # Se senaste sessionslogg  
cat systemmonitor/Storage/log-*.txt       # Se händelselogg  

---

## 🔄 Git – versionshantering

git status                   # Kolla vilka filer som är ändrade  
git add .                    # Lägg till alla ändringar i staging  
git commit -m "Din kommentar" # Skapa commit med meddelande  
git push origin main          # Skicka upp till GitHub  
git pull origin main          # Hämta senaste ändringar från GitHub  

---

## ✅ Tips & Tricks

- Använd Tab för autokomplettering av fil- och mappnamn.  
- Använd ↑ och ↓ för att bläddra i tidigare körda kommandon.  
- Kontrollera alltid vilken mapp du befinner dig i med pwd innan du kör kommandon.  
- Om något krånglar: börja med att lista filer (ls) och säkerställ att du är i rätt mapp.  
- Loggar och sessionsfiler finns alltid i systemmonitor/Storage.  