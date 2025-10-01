from dataclasses import dataclass
from enum import Enum
from typing import List
from pathlib import Path
import json

ALARM_FILE = Path("alarms.json")

class AlarmType(Enum):
    CPU = "CPU"
    MEM = "MINNE"
    DISK = "DISK"

    @property
    def display_name(self) -> str:
        return {"CPU": "CPU larm", "MINNE": "Minneslarm", "DISK": "Disklarm"}[self.value]

@dataclass(frozen=True)
class Alarm:
    type: AlarmType
    threshold: int  # 1..100

class AlarmStore:
    """Lagrar larm i JSON"""
    def __init__(self):
        self._alarms: List[Alarm] = []
        self.load()  # ladda vid start

    def load(self) -> None:
        if not ALARM_FILE.exists():
            self._alarms = []
            return
        data = json.loads(ALARM_FILE.read_text(encoding="utf-8"))
        self._alarms = [Alarm(AlarmType(o["type"]), int(o["threshold"])) for o in data]

    def save(self) -> None:
        payload = [{"type": a.type.value, "threshold": a.threshold} for a in self._alarms]
        ALARM_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # CRUD
    def add(self, type_: AlarmType, threshold: int) -> None:
        self._alarms.append(Alarm(type_, threshold))
        self._alarms.sort(key=lambda a: (a.type.value, a.threshold))
        self.save()

    def list_sorted(self) -> List[Alarm]:
        return sorted(self._alarms, key=lambda a: (a.type.value, a.threshold))

    def all(self) -> List[Alarm]:
        return list(self._alarms)
