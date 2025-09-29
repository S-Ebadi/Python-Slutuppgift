from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional


class AlarmType(Enum):
    CPU = auto()
    MEMORY = auto()
    DISK = auto()

    def display(self) -> str:
        return {
            AlarmType.CPU: "CPU",
            AlarmType.MEMORY: "Minnes",
            AlarmType.DISK: "Disk",
        }[self]


@dataclass
class Alarm:
    type: AlarmType
    threshold: int  # 1..100


class AlarmRegistry:
    def __init__(self, initial: List[dict] | None = None):
        self._alarms: List[Alarm] = []
        if initial:
            for a in initial:
                # Backward-säker: tillåt str eller int threshold, map typ
                atype = AlarmType[a["type"]] if isinstance(a["type"], str) else a["type"]
                self._alarms.append(Alarm(atype, int(a["threshold"])) )

    # --- CRUD ---
    def add_alarm(self, atype: AlarmType, threshold: int) -> None:
        self._alarms.append(Alarm(atype, int(threshold)))

    def get_sorted(self) -> List[Alarm]:
        # Funktionell sortering per kravspec: sortera på typ-namn, sedan tröskel
        return sorted(self._alarms, key=lambda a: (a.type.name, a.threshold))

    def remove_by_sorted_index(self, idx: int) -> Optional[Alarm]:
        sorted_list = self.get_sorted()
        if 0 <= idx < len(sorted_list):
            target = sorted_list[idx]
            # Hitta första match och ta bort ur original-listan
            for i, a in enumerate(self._alarms):
                if a.type == target.type and a.threshold == target.threshold:
                    return self._alarms.pop(i)
        return None

    def as_dict_list(self) -> List[dict]:
        return [{"type": a.type.name, "threshold": int(a.threshold)} for a in self._alarms]

    # --- Triggerlogik (VG: endast närmaste per typ) ---
    def closest_trigger(self, atype: AlarmType, current_value: float) -> Optional[Alarm]:
        # Filtrera alla larm av given typ där tröskel <= aktuellt värde
        candidates = [a for a in self._alarms if a.type == atype and a.threshold <= current_value]
        if not candidates:
            return None
        # Välj högsta tröskel (närmast current_value underifrån)
        return max(candidates, key=lambda a: a.threshold)
