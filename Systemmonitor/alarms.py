import json, os, uuid

# Alla larm sparas i en JSON-fil under Storage/
storage_dir = os.path.join(os.path.dirname(__file__), "Storage")
os.makedirs(storage_dir, exist_ok=True)
alarms_file = os.path.join(storage_dir, "alarms.json")

def load():
    """Laddar alla larm från JSON-filen."""
    if os.path.exists(alarms_file):
        try:
            with open(alarms_file, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save(data):
    """Sparar alla larm till JSON-filen."""
    with open(alarms_file, "w") as f:
        json.dump(data, f, indent=2)

def list_all():
    """Returnerar alla larm som lista."""
    return load()

def create(metric, threshold, direction=">="):
    """Skapar nytt larm och sparar det i filen."""
    data = load()
    alarm = {
        "id": str(uuid.uuid4()), 
        "metric": metric, 
        "threshold": threshold, 
        "direction": direction
    }
    data.append(alarm)
    save(data)
    return alarm

def update(alarm_id, **kwargs):
    """Uppdaterar ett larm (t.ex. threshold)."""
    data = load()
    for a in data:
        if a["id"] == alarm_id:
            a.update(kwargs)
    save(data)

def delete(alarm_id):
    """Tar bort ett larm med valt ID."""
    data = load()
    data = [a for a in data if a["id"] != alarm_id]
    save(data)

def evaluate(cpu, mem, disk):
    """Kollar om något larm triggas baserat på aktuella värden."""
    hits = []
    for a in load():
        # Bestäm vilket värde som ska jämföras
        if a["metric"] == "cpu":
            value = cpu
        elif a["metric"] == "memory":
            value = mem
        elif a["metric"] == "disk":
            value = disk
        else:
            continue

        # Jämför mot threshold
        if a["direction"] == ">=" and value >= a["threshold"]:
            hits.append(a)
    return hits
