import os, datetime

# Skapa Storage-mappen om den inte finns
STORAGE_DIR = os.path.join(os.path.dirname(__file__), "Storage")
os.makedirs(STORAGE_DIR, exist_ok=True)

# Skapa loggfil med tidsstämpel (ny för varje körning)
ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
LOG_FILE = os.path.join(STORAGE_DIR, f"log-{ts}.txt")


def log(event: str):
    """
    Logga en händelse med tidsstämpel.
    Exempel: "2025-10-02 21:15:32 - Larm CPU 80% triggat"
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now} - {event}"
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")
