import math
import sys
import time
from typing import Callable

# POSIX: non-blocking enter-detection
try:
    import select  # type: ignore
except Exception:
    select = None


def ask_int_in_range(prompt: str, lo: int, hi: int) -> int:
    while True:
        s = input(prompt).strip()
        try:
            val = int(s)
            if lo <= val <= hi:
                return val
            print(f"Mata in en siffra mellan {lo}-{hi}.")
        except ValueError:
            print("Ogiltig siffra. Försök igen.")


def press_enter_to_continue():
    input("\nTryck Enter för att gå tillbaka till huvudmenyn...")


def format_bytes(n: int) -> str:
    if n < 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    if n == 0:
        return "0 B"
    i = min(int(math.log(n, 1024)), len(units) - 1)
    val = n / (1024 ** i)
    return f"{val:.1f} {units[i]}"


def nonblocking_enter_loop(tick: Callable[[], None], interval_sec: float = 1.0):
    """
    Kör tick() periodiskt. Avslutas när användaren trycker Enter.
    POSIX: använder select på sys.stdin. På plattform utan select faller vi tillbaka
    till blockande input med hint i konsolen.
    """
    if select is None:
        # Fallback – enklare variant
        print("(Tryck Enter för att avsluta övervakningsläge)")
        try:
            while True:
                tick()
                time.sleep(interval_sec)
        except KeyboardInterrupt:
            return
        finally:
            input()  # enter för att lämna
    else:
        try:
            while True:
                tick()
                # Vänta upp till intervallet på Enter
                rlist, _, _ = select.select([sys.stdin], [], [], interval_sec)
                if sys.stdin in rlist:
                    _ = sys.stdin.readline()
                    break
        except KeyboardInterrupt:
            return
