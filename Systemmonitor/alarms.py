import os, json, uuid

# Skapa Storage-mapp om den inte finns
STORAGE_DIR = os.path.join(os.path.dirname(__file__), "Storage")
os.makedirs(STORAGE_DIR, exist_ok=True)

ALARMS_FILE = os.path.join(STORAGE_DIR, "alarms.json")

def load():
    if not os.path.exists(ALARMS_FILE):
        return []
    try:
        with open(ALARMS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save(alarms):
    with open(ALARMS_FILE, "w") as f:
        json.dump(alarms, f, indent=2)

def list_all():
    return load()

def create(metric, threshold, direction):
    alarms = load()
    a = {"id": str(uuid.uuid4()), "metric": metric, "threshold": threshold, "direction": direction}
    alarms.append(a)
    save(alarms)
    return a

def update(id, **kwargs):
    alarms = load()
    for a in alarms:
        if a["id"] == id:
            a.update(kwargs)
    save(alarms)

def delete(id):
    alarms = [a for a in load() if a["id"] != id]
    save(alarms)

def evaluate(cpu, mem, disk):
    """Returnerar lista av larm som har triggats"""
    hits = []
    for a in load():
        val = cpu if a["metric"]=="cpu" else mem if a["metric"]=="memory" else disk
        if a["direction"] == ">=" and val >= a["threshold"]:
            hits.append(a)
    return hits
