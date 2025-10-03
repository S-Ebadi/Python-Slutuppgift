import json, os, uuid
import logger

# Alla larm sparas i Storage/
storage_dir = os.path.join(os.path.dirname(__file__), "Storage")
os.makedirs(storage_dir, exist_ok=True)
alarms_file = os.path.join(storage_dir, "alarms.json")

def load():
    if os.path.exists(alarms_file):
        try:
            with open(alarms_file, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save(data):
    with open(alarms_file, "w") as f:
        json.dump(data, f, indent=2)

def list_all():
    return load()

def create(metric, threshold, direction=">="):
    data = load()
    alarm = {
        "id": str(uuid.uuid4()),
        "metric": metric,
        "threshold": threshold,
        "direction": direction
    }
    data.append(alarm)
    save(data)
    logger.log_event(f"Nytt larm skapat: {metric.upper()} {direction} {threshold}%")
    return alarm

def update(alarm_id, **kwargs):
    data = load()
    for a in data:
        if a["id"] == alarm_id:
            a.update(kwargs)
            logger.log_event(f"Larm uppdaterat: {a['metric'].upper()} -> {a}")
    save(data)

def delete(alarm_id):
    data = load()
    target = None
    for a in data:
        if a["id"] == alarm_id:
            target = a
    data = [a for a in data if a["id"] != alarm_id]
    save(data)
    if target:
        logger.log_event(f"Larm borttaget: {target['metric'].upper()} {target['threshold']}%")

def evaluate(cpu, mem, disk):
    hits = []
    for a in load():
        if a["metric"] == "cpu":
            value = cpu
        elif a["metric"] == "memory":
            value = mem
        elif a["metric"] == "disk":
            value = disk
        else:
            continue

        if a["direction"] == ">=" and value >= a["threshold"]:
            hits.append(a)
    return hits
