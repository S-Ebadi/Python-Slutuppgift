from datetime import datetime
from pathlib import Path

_log_file = None


def init_logger():
    global _log_file
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    Path("logs").mkdir(exist_ok=True)
    _log_file = Path("logs") / f"systemmonitor_{ts}.log"


def _timestamp() -> str:
    return datetime.now().strftime("%d/%m/%Y_%H:%M")


def log_event(message: str):
    if _log_file is None:
        return
    line = f"{_timestamp()}_{message}\n"
    with _log_file.open("a", encoding="utf-8") as f:
        f.write(line)
