from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
import json
from pathlib import Path
import logging

ALARM_FILE = Path("alarms.json")

class AlarmType(Enum):
    CPU = "CPU"
    MEM = "MINNE"
    DISK = "DISK"

    @property
    def display_name(self) -> str:
        if self is AlarmType.CPU:
            return "CPU larm"
        if self is AlarmType.MEM:
            return "Minneslarm"
        return "Disklarm"

@dataclass(frozen=True)
class Alarm:
    type: AlarmType
    threshold: int  # 1..100

class AlarmManager:
    def __init__(self, logger: Optional[logging.Logger] = None):
        self._alarms: List[Alarm] = []
        self.logger = logger

    # Persistens
    def load(self):
        if not ALARM_FILE.exists():
            return
        try:
            data = json.loads(ALARM_FILE.read_text(encoding="utf-8"))
            items = []
            for obj in data:
                t = AlarmType(obj["type"])
                thr = int(obj["threshold"])
                items.append(Alarm(type=t, threshold=thr))
            self._alarms = items
            if self.logger:
                self.logger.info("Alarmlista_inlast")
        except Exception as e:
            if self.logger:
                self.logger.error(f"Fel_vid_inlasning_alarms.json_{e}")

    def save(self):
        data = [{"type": a.type.value, "threshold": a.threshold} for a in self._alarms]
        ALARM_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        if self.logger:
            self.logger.info("Alarmlista_sparad")

    # CRUD
    def add_alarm(self, type_: AlarmType, threshold: int) -> None:
        self._alarms.append(Alarm(type=type_, threshold=threshold))
        self._alarms.sort(key=lambda a: (a.type.value, a.threshold))
        self.save()

    def remove_alarm(self, alarm: Alarm) -> None:
        self._alarms = [a for a in self._alarms if a != alarm]
        self.save()

    def list_sorted(self) -> List[Alarm]:
        # Funktionell stil: sorterat med lambda-key
        return sorted(self._alarms, key=lambda a: (a.type.value, a.threshold))

    # Larmtriggers – endast "närmast över tröskel" per typ ska trigga.
    def _closest_trigger_for_type(self, current: float, type_: AlarmType) -> Optional[int]:
        # Ta alla thresholds <= current och returnera den HÖGSTA (närmast)
        thresholds = [a.threshold for a in self._alarms if a.type == type_ and current >= a.threshold]
        return max(thresholds) if thresholds else None

    def check_triggers(self, *, cpu: float, mem: float, disk: float) -> List[str]:
        triggers: List[str] = []

        def fmt(type_: AlarmType, thr: int) -> str:
            # Exakt logg-/textformat enligt uppgiftsstil
            if type_ is AlarmType.CPU:
                return f"CPU Användningslarm aktiverat {thr} Procent"
            if type_ is AlarmType.MEM:
                return f"Minnesanvändningslarm aktiverat {thr} Procent"
            return f"Diskanvändningslarm aktiverat {thr} Procent"

        cpu_thr = self._closest_trigger_for_type(cpu, AlarmType.CPU)
        if cpu_thr is not None:
            triggers.append(fmt(AlarmType.CPU, cpu_thr))

        mem_thr = self._closest_trigger_for_type(mem, AlarmType.MEM)
        if mem_thr is not None:
            triggers.append(fmt(AlarmType.MEM, mem_thr))

        disk_thr = self._closest_trigger_for_type(disk, AlarmType.DISK)
        if disk_thr is not None:
            triggers.append(fmt(AlarmType.DISK, disk_thr))

        return triggers
