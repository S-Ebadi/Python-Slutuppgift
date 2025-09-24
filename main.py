from menu import Menu
from alarms import AlarmManager
from pathlib import Path
import logging
from datetime import datetime

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def _configure_logging() -> logging.Logger:
    """
    Skapar en ny loggfil per programstart.
    Format enligt kravet: DD/MM/YYYY_HH:MM_<EventText>
    """
    log_name = datetime.now().strftime("monitor_%Y%m%d_%H%M%S.log")
    log_path = LOG_DIR / log_name

    logger = logging.getLogger("systemmonitor")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    class StrictFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            ts = datetime.now().strftime("%d/%m/%Y_%H:%M")
            return f"{ts}_{record.getMessage()}"

    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(StrictFormatter())
    logger.addHandler(fh)

    # Minimal konsol-echo för användaren (ingen extra formattering).
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)  # håll tyst i konsol utom vid fel
    logger.addHandler(ch)

    return logger

def main():
    logger = _configure_logging()
    logger.info("Program_startat")

    # Ladda persisterade larm
    am = AlarmManager(logger=logger)
    am.load()
    print("Loading previously configured alarms...")

    menu = Menu(alarm_manager=am, logger=logger)
    menu.run()

if __name__ == "__main__":
    main()
