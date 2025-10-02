import sys, time, os, json, datetime, threading
import monitor
from alarms import AlarmStore
import utils
import logger

store = AlarmStore()
monitoring_active = False
last_status = {}
session_log = []


def start_overvakning():
    """Aktivt övervakningsläge: mäter kontinuerligt, triggar larm och sparar logg."""
    global monitoring_active, last_status, session_log
    monitoring_active = True
    session_log = []
    print("\nÖvervakning startad. Tryck Enter för att avsluta.\n")
    logger.log("Övervakning startad")

    stop_flag = {"stop": False}
    def wait_for_enter():
        input()
        stop_flag["stop"] = True
    threading.Thread(target=wait_for_enter, daemon=True).start()

    while monitoring_active and not stop_flag["stop"]:
        cpu = monitor.read_cpu()
        mem = monitor.read_memory()
        disk = monitor.read_disk()
        last_status = {"cpu": cpu, "mem": mem.percent, "disk": disk.percent}

        sys.stdout.write(
            f"\rCPU {cpu:.0f}% | Minne {mem.percent:.0f}% ({utils.gb(mem.used):.1f} GB / {utils.gb(mem.total):.1f} GB) | "
            f"Disk {disk.percent:.0f}% ({utils.gb(disk.used):.1f} GB / {utils.gb(disk.total):.1f} GB)   "
        )
        sys.stdout.flush()

        # Kolla larm
        for metric, val in last_status.items():
            alarm = store.get_relevant(metric, val)
            if alarm:
                msg = f"LARM: {metric.upper()} över {alarm['threshold']}%"
                print(f"\n*** {msg} ***")
                logger.log(msg)
                utils.beep(1, 0.2)

        session_log.append({
            "cpu": cpu,
            "mem": mem.percent,
            "disk": disk.percent,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

        time.sleep(1)

    monitoring_active = False
    print("\nAvslutar övervakning...")
    logger.log("Övervakning stoppad")

    # --- Spara logg med tidsstämpel i Storage ---
    storage_dir = os.path.join(os.path.dirname(__file__), "Storage")
    os.makedirs(storage_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_file = os.path.join(storage_dir, f"session-{ts}.json")
    with open(log_file, "w") as f:
        json.dump(session_log, f, indent=2)
    print(f"Senaste session sparad till {log_file}")


def list_active():
    """Visar status om övervakning är igång."""
    if not monitoring_active:
        print("\nIngen övervakning är aktiv.")
    else:
        print("\n— Aktiv övervakning —")
        print(f"CPU: {last_status.get('cpu',0):.0f}%")
        print(f"Minne: {last_status.get('mem',0):.0f}%")
        print(f"Disk: {last_status.get('disk',0):.0f}%")
    utils.press()


def create_alarm():
    """Meny för att skapa larm enligt instruktionerna."""
    print("\n=== Skapa larm ===")
    metric = utils.choice("Välj metric:", ["cpu", "disk", "mem"])
    thr = utils.fnum("Ställ in nivå (1–100): ", 1, 100)
    store.add(metric, thr)
    logger.log(f"Larm skapat: {metric} {thr}%")
    print(f"Larm för {metric.upper()} satt till {thr:.0f}%.")
    utils.press()


def show_alarms():
    """Visar alla larm, sorterade på typ."""
    L = store.list()
    if not L:
        print("\nInga larm."); utils.press(); return
    print("\n— Larm —")
    for i,a in enumerate(L,1):
        print(f"{i}. {a['metric'].upper()} larm {a['threshold']:.0f}%")
    utils.press()


def edit_alarm():
    """Ändra eller ta bort ett larm."""
    L = store.list()
    if not L:
        print("Inga larm."); utils.press(); return

    print("\n— Välj larm att ändra/ta bort —")
    for i,a in enumerate(L,1):
        print(f"{i}. {a['metric'].upper()} larm {a['threshold']:.0f}%")
    s = input("Nummer: ").strip()
    if not s.isdigit() or not (1 <= int(s) <= len(L)):
        print("Fel val."); return
    idx = int(s)-1

    f = input("t = ändra threshold, d = ta bort: ").strip().lower()
    if f == "t":
        thr = utils.fnum("Ny nivå (1–100): ", 1, 100)
        store.update(idx, thr)
        logger.log(f"Larm uppdaterat: {idx} → {thr}%")
        print("Uppdaterat.")
    elif f == "d":
        store.remove(idx)
        logger.log(f"Larm raderat: {idx}")
        print("Borttaget.")
    else:
        print("Fel val.")
    utils.press()


def show_last_results():
    """Visar resultat från senaste övervakningen."""
    if not session_log:
        print("\nIngen övervakning har körts än.")
        utils.press(); return

    print("\n=== Senaste övervakning ===")
    print(f"Totalt antal mätpunkter: {len(session_log)}")
    print(f"Totalt antal larm: (se loggfil för detaljer)")
    print("\nSista mätpunkterna:")
    for row in session_log[-5:]:
        print(f"CPU {row['cpu']:.0f}%, Minne {row['mem']:.0f}%, Disk {row['disk']:.0f}%")
    utils.press()


def main():
    actions = [
        ("Starta övervakning", start_overvakning),
        ("Lista aktiv övervakning", list_active),
        ("Skapa larm", create_alarm),
        ("Visa larm", show_alarms),
        ("Ändra/Ta bort larm", edit_alarm),
        ("Visa senaste övervakningsresultat", show_last_results),
        ("Avsluta", None),
    ]
    while True:
        print("\n=== Huvudmeny ===")
        for i,(lbl,_) in enumerate(actions,1):
            print(f"{i}. {lbl}")
        s = input("Välj: ").strip()
        if not s.isdigit() or not (1 <= int(s) <= len(actions)):
            print("Fel val."); continue
        _, fn = actions[int(s)-1]
        if fn is None:
            print("Avslutar..."); break
        fn()


if __name__=="__main__":
    main()
