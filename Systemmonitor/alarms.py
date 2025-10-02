import json, uuid
from pathlib import Path

FILE = Path("alarms.json")

def _load():
    if not FILE.exists(): return []
    try: return json.loads(FILE.read_text(encoding="utf-8"))
    except: return []

def _save(items): FILE.write_text(json.dumps(items, indent=2), encoding="utf-8")

def list_all(): return _load()

def create(metric, threshold, direction, description=""):
    items = _load()
    a = {"id": str(uuid.uuid4()), "metric": metric, "threshold": float(threshold),
         "direction": direction, "description": description}
    items.append(a); _save(items); return a

def get(aid):
    return next((a for a in _load() if a["id"] == aid), None)

def update(aid, **fields):
    items = _load()
    for a in items:
        if a["id"] == aid:
            a.update({k:v for k,v in fields.items() if v is not None})
            _save(items); return True
    return False

def delete(aid):
    items = _load()
    n = len(items)
    items = [a for a in items if a["id"] != aid]
    if len(items) != n: _save(items); return True
    return False

def evaluate(cpu_pct, mem_pct, disk_pct):
    hits = []
    val = {"cpu": cpu_pct, "memory": mem_pct, "disk": disk_pct}
    for a in _load():
        x = val[a["metric"]]
        if (a["direction"] == ">=" and x >= a["threshold"]) or (a["direction"] == "<=" and x <= a["threshold"]):
            hits.append(a)
    return hits
