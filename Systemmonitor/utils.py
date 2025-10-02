import sys, time

def gb(b): return b/1024**3

def press(): input("\nTryck Enter för att fortsätta...")

def choice(prompt, opts):
    while True:
        print(prompt); [print(f"{i+1}. {o}") for i,o in enumerate(opts)]
        s = input("Välj: ").strip()
        if s.isdigit() and 1 <= int(s) <= len(opts): return opts[int(s)-1]
        print("Ogiltigt val.")

def fnum(prompt, lo=None, hi=None):
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            x = float(s)
            if (lo is None or x>=lo) and (hi is None or x<=hi): return x
        except: pass
        print("Ogiltigt tal.")

def spinner(i): return "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"[i%10]

def led(on, label=""): return f"{('#' if on else '-') } {label}".strip()

def clr_line():
    sys.stdout.write("\r"); sys.stdout.write(" " * 120); sys.stdout.write("\r"); sys.stdout.flush()

def beep(times=1, interval=0.1):
    try:
        for _ in range(times):
            sys.stdout.write("\a"); sys.stdout.flush(); time.sleep(interval)
    except: pass
