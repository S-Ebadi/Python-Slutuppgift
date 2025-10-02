import sys, time

def gb(b):
    """Konvertera bytes till gigabyte."""
    return b / 1024**3

def press():
    """Pausa tills användaren trycker Enter."""
    input("\nTryck Enter för att fortsätta...")

def choice(prompt, opts):
    """Visa en lista med alternativ och returnera valt objekt."""
    while True:
        print(prompt)
        [print(f"{i+1}. {o}") for i,o in enumerate(opts)]
        s = input("Välj: ").strip()
        if s.isdigit() and 1 <= int(s) <= len(opts):
            return opts[int(s)-1]
        print("Ogiltigt val.")

def fnum(prompt, lo=None, hi=None):
    """Be om ett flyttal inom (lo, hi)."""
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            x = float(s)
            if (lo is None or x >= lo) and (hi is None or x <= hi):
                return x
        except:
            pass
        print("Ogiltigt tal.")

def spinner(i):
    """Returnera en snurrande symbol (för progressindikator)."""
    return "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"[i % 10]

def led(on, label=""):
    """Simulera LED-indikator (# = på, - = av)."""
    return f"{('#' if on else '-') } {label}".strip()

def clr_line():
    """Rensa nuvarande terminalrad."""
    sys.stdout.write("\r")
    sys.stdout.write(" " * 120)
    sys.stdout.write("\r")
    sys.stdout.flush()
