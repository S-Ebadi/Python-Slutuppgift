import json
from pathlib import Path
from typing import List, Optional

_DEFAULT_PATH = Path("alarms.json")


def load_alarms(path: Optional[Path] = None) -> List[dict]:
    p = path or _DEFAULT_PATH
    if not p.exists():
        return []
    try:
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except Exception:
        # Korrupt fil – återställ säkert läge
        return []


def save_alarms(alarms: List[dict], path: Optional[Path] = None) -> None:
    p = path or _DEFAULT_PATH
    with p.open("w", encoding="utf-8") as f:
        json.dump(alarms, f, ensure_ascii=False, indent=2)
