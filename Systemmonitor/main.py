import sys, time, os, json, datetime, threading
import monitor
import alarms
import utils
import logger

monitoring_active = False
last_status = {}
session_log = []

def start_overvakning():
    global monitoring_active, last_status, session_log
    monitoring_active = True
    session_log = []
    print("\nÖvervakning startad. Tryck Enter för att avsluta.\n")
    logger.log_event("Övervakning startad")

    stop_flag = {"stop": False}
    def wait_for_enter():
        input()
        stop_flag["stop"] = True
    threading.Thread(target=wait_for_enter, daemon=True).start()

    while monitoring_active and not stop_flag["stop"]:
        cpu = monitor.read_cpu()
        mem_pct, mem_used, mem_total = monitor.read_memory()
        disk_pct, disk_used, disk_total = monitor.read_disk()
        last_status = {"cpu": cpu, "mem": mem_pct, "disk": disk_pct}

        sys.stdout.write(
            f"\rCPU {cpu:.0f}% | Minne {mem_pct:.0f}% ({utils.gb(mem_used):.1f} GB / {utils.gb(mem_total):.1f} GB) | "
            f"Disk {disk_pct:.0f}% ({utils.gb(disk_used):.1f} GB / {utils.gb(disk_total):.1f} GB)   "
        )
        sys.stdout.flush()

        hits = alarms.evaluate(cpu, mem_pct, disk_pct)
        alarms_triggered = []
        for a in hits:
            msg = f"LARM: {a['metric'].upper()} {a['direction']} {a['threshold']:.0f}%"
            alarms_triggered.append(msg)
            print(f"\n*** {msg} ***")
            logger.log_event(f"{msg} triggat")

        session_log.append({
            "cpu": cpu,
            "mem": mem_pct,
            "disk": disk_pct,
            "alarms": alarms_triggered,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

        time.sleep(1)

    monitoring_active = False
    print("\nAvslutar övervakning...")
    logger.log_event("Övervakning avslutad")

    storage_dir = os.path.join(os.path.dirname(__file__), "Storage")
    os.makedirs(storage_dir, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_file = os.path.join(storage_dir, f"session-{ts}.json")
    with open(log_file, "w") as f:
        json.dump(session_log, f, indent=2)
    print(f"Senaste session sparad till {log_file}")
    logger.log_event(f"Session sparad: {log_file}")

def list_active():
    if not monitoring_active:
        print("\nIngen övervakning är aktiv.")
    else:
        print("\n— Aktiv övervakning —")
        print(f"CPU: {last_status.get('cpu',0):.0f}%")
        print(f"Minne: {last_status.get('mem',0):.0f}%")
        print(f"Disk: {last_status.get('disk',0):.0f}%")
    utils.press()

def create_alarm():
    print("\n=== Skapa larm ===")
    print("1. CPU (1–100)")
    print("2. Disk (1–100)")
    print("3. Memory (1–100)")
    choice = input("Välj: ").strip()

    if choice == "1": metric = "cpu"
    elif choice == "2": metric = "disk"
    elif choice == "3": metric = "memory"
    else: print("Fel val."); return

    t = input(f"Ställ in nivå för {metric.upper()} (1–100): ").strip()
    if not t.isdigit() or not (1 <= int(t) <= 100):
        print("Felaktig nivå."); return

    t = float(t)
    a = alarms.create(metric, t, ">=")
    print(f"Larm för {metric.upper()} satt till {t:.0f}%. (ID {a['id']})")
    utils.press()

def show_alarms():
    L = sorted(alarms.list_all(), key=lambda a: a["metric"])
    if not L:
        print("\nInga larm."); utils.press(); return
    print("\n— Larm —")
    for i,a in enumerate(L,1):
        print(f"{i}. {a['metric'].upper()} larm {a['threshold']:.0f}% (ID {a['id']})")
    utils.press()

def edit_alarm():
    L = alarms.list_all()
    if not L:
        print("Inga larm."); utils.press(); return
    print("\n— Välj larm att ändra/ta bort —")
    for i,a in enumerate(L,1):
        print(f"{i}. {a['metric'].upper()} larm {a['threshold']:.0f}% (ID {a['id']})")
    s = input("Nummer: ").strip()
    if not s.isdigit() or not (1 <= int(s) <= len(L)):
        print("Fel val."); return
    a = L[int(s)-1]
    f = input("t = ändra threshold, d = ta bort: ").strip().lower()
    if f == "t":
        n = input("Ny nivå (1–100): ").strip()
        if n.isdigit() and 1 <= int(n) <= 100:
            alarms.update(a["id"], threshold=float(n))
            print("Uppdaterat.")
        else:
            print("Felaktig nivå.")
    elif f == "d":
        alarms.delete(a["id"])
        print("Borttaget.")
    else:
        print("Fel val.")
    utils.press()

def show_last_results():
    if not session_log:
        print("\nIngen övervakning har körts än.")
        utils.press(); return
    print("\n=== Senaste övervakning ===")
    print(f"Totalt antal mätpunkter: {len(session_log)}")
    alarms_total = sum(len(x["alarms"]) for x in session_log)
    print(f"Totalt antal larm: {alarms_total}")
    print("\nSista mätpunkterna:")
    for row in session_log[-5:]:
        print(f"CPU {row['cpu']:.0f}%, Minne {row['mem']:.0f}%, Disk {row['disk']:.0f}%")
        for alarm in row["alarms"]:
            print(f"   -> {alarm}")
    utils.press()

def overvakningslage():
    print("\nÖvervakningsläge startat. Tryck Enter för att återgå till menyn.\n")
    logger.log_event("Övervakningsläge startat")
    stop_flag = {"stop": False}
    def wait_for_enter():
        input()
        stop_flag["stop"] = True
    threading.Thread(target=wait_for_enter, daemon=True).start()
    while not stop_flag["stop"]:
        cpu = monitor.read_cpu()
        mem_pct,_,_ = monitor.read_memory()
        disk_pct,_,_ = monitor.read_disk()
        sys.stdout.write(
            f"\rCPU {cpu:.0f}% | Minne {mem_pct:.0f}% | Disk {disk_pct:.0f}%   "
        )
        sys.stdout.flush()
        time.sleep(1)
    logger.log_event("Övervakningsläge avslutat")

def main():
    actions = [
        ("Starta övervakning", start_overvakning),
        ("Lista aktiv övervakning", list_active),
        ("Skapa larm", create_alarm),
        ("Visa larm", show_alarms),
        ("Ändra/Ta bort larm", edit_alarm),
        ("Visa senaste övervakningsresultat", show_last_results),
        ("Övervakningsläge", overvakningslage),
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
