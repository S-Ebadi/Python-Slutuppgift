import sys, time, select
from typing import Callable

def ask_int_in_range(prompt: str, low: int, high: int) -> int:
    while True:
        try:
            v = int(input(prompt))
            if low <= v <= high:
                return v
            print(f"Värdet måste vara mellan {low}-{high}.")
        except (ValueError, KeyboardInterrupt):
            print("Ogiltig inmatning. Försök igen.")

def press_enter_to_continue():
    input("Tryck Enter för att gå tillbaka till huvudmenyn...")

def format_bytes(n: int) -> str:
    gb = n / (1024**3)
    return f"{gb:.1f} GB"

def nonblocking_enter_loop(tick: Callable[[], None], interval_sec: float = 1.0):
    """Kör tick() periodiskt tills användaren trycker Enter (POSIX/macOS/Linux)."""
    print("Övervakning är aktiv, tryck Enter för att återgå till menyn.")
    try:
        while True:
            tick()
            if sys.platform != "win32":
                dr, _, _ = select.select([sys.stdin], [], [], interval_sec)
                if dr:
                    sys.stdin.readline()
                    break
            else:
                time.sleep(interval_sec)
    except KeyboardInterrupt:
        pass
