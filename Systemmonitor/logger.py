import os, datetime

storage_dir = os.path.join(os.path.dirname(__file__), "Storage")
os.makedirs(storage_dir, exist_ok=True)

def log_event(event):
    """Skriver en händelse till en daglig loggfil i Storage/."""
    ts = datetime.datetime.now().strftime("%Y%m%d")
    logfile = os.path.join(storage_dir, f"log-{ts}.txt")
    with open(logfile, "a") as f:
        f.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} - {event}\n")
