from monitor import read_cpu_percent, read_memory, read_disk
from alarms import AlarmType, AlarmStore
from utils import ask_int_in_range, press_enter_to_continue, format_bytes, nonblocking_enter_loop

store = AlarmStore()          # laddar tidigare larm från alarms.json
monitoring_active = False     # för "Lista aktiv övervakning"

def show_status():
    """Visar om övervakning är aktiv, och i så fall aktuell status (utan larm)."""
    print("\n--- Aktiv övervakning ---")
    if not monitoring_active:
        print("Ingen övervakning är aktiv.")
    else:
        cpu = read_cpu_percent()
        mem = read_memory()
        disk = read_disk()
        print(f"CPU Anvädning: {cpu:.0f}%")
        print(f"Minnesanvändning: {mem['percent']:.0f}% ({format_bytes(mem['used'])} out of {format_bytes(mem['total'])} used)")
        print(f"Diskanvändning: {disk['percent']:.0f}% ({format_bytes(disk['used'])} out of {format_bytes(disk['total'])} used)")
    press_enter_to_continue()

def configure_alarm():
    print("\n--- Konfigurera larm ---")
    print("1. CPU användning")
    print("2. Minnesanvändning")
    print("3. Diskanvändning")
    print("4. Tillbaka till huvudmeny")
    val = ask_int_in_range("Välj typ (1-4): ", 1, 4)
    if val == 4:
        return
    typ_map = {1: AlarmType.CPU, 2: AlarmType.MEM, 3: AlarmType.DISK}
    atype = typ_map[val]
    thr = ask_int_in_range("Ställ in nivå för alarm mellan 1-100: ", 1, 100)
    store.add(atype, thr)
    print(f"Larm för {atype.value} användning satt till {thr}%.")
    press_enter_to_continue()

def show_alarms():
    print("\n--- Aktiva larm ---")
    current = store.list_sorted()
    if not current:
        print("Inga larm konfigurerade.")
    else:
        for a in current:
            print(f"{a.type.display_name} {a.threshold}%")
    press_enter_to_continue()

def start_monitoring():
    global monitoring_active
    monitoring_active = True
    print("\n--- Övervakningsläge ---")
    print("Tryck Enter för att avsluta.")

    def tick():
        cpu = read_cpu_percent()
        mem = read_memory()
        disk = read_disk()
        print(f"CPU: {cpu:.1f}% | Minne: {mem['percent']:.1f}% | Disk: {disk['percent']:.1f}%", end=" ")
        # Enkel G-nivå: trigga alla larm vars tröskel passeras
        for a in store.list_sorted():
            if a.type == AlarmType.CPU and cpu >= a.threshold:
                print(f"\n***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER {a.threshold}%***", end=" ")
            if a.type == AlarmType.MEM and mem['percent'] >= a.threshold:
                print(f"\n***VARNING, LARM AKTIVERAT, MINNESANVÄNDNING ÖVERSTIGER {a.threshold}%***", end=" ")
            if a.type == AlarmType.DISK and disk['percent'] >= a.threshold:
                print(f"\n***VARNING, LARM AKTIVERAT, DISKANVÄNDNING ÖVERSTIGER {a.threshold}%***", end=" ")
        print()

    nonblocking_enter_loop(tick, interval_sec=1.0)
    print("\nAvslutar övervakning.")
    monitoring_active = False
    press_enter_to_continue()

def main_menu():
    actions = [
        ("Starta övervakning", start_monitoring),
        ("Lista aktiv övervakning", show_status),
        ("Skapa larm", configure_alarm),
        ("Visa larm", show_alarms),
        ("Avsluta", None),
    ]

    while True:
        print("\n--- Huvudmeny ---")
        for idx, (title, _) in enumerate(actions, 1):
            print(f"{idx}. {title}")
        try:
            choice = int(input("Välj ett alternativ (1-5): "))
        except (ValueError, KeyboardInterrupt):
            print("Ogiltigt val.")
            continue
        if not (1 <= choice <= len(actions)):
            print("Ogiltigt val.")
            continue
        title, fn = actions[choice - 1]
        if fn is None:
            print("Avslutar programmet.")
            break
        fn()

if __name__ == "__main__":
    print("Loading previously configured alarms...")
    main_menu()
