import sys, time
import monitor
import alarms

monitoring_active = False
last_status = {}
session_log = []  # sparar senaste övervakningens mätningar och larm

def press():
    input("\nTryck Enter för att fortsätta...")

def start_overvakning():
    """Aktivt övervakningsläge: mäter kontinuerligt och triggar larm, stoppas med Enter."""
    global monitoring_active, last_status, session_log
    monitoring_active = True
    session_log = []  # rensa gammal logg
    print("\nÖvervakning startad. Tryck Enter för att avsluta.\n")

    import threading
    stop_flag = {"stop": False}

    def wait_for_enter():
        input()
        stop_flag["stop"] = True

    threading.Thread(target=wait_for_enter, daemon=True).start()

    i = 0
    while monitoring_active and not stop_flag["stop"]:
        cpu = monitor.cpu()
        mem_pct, mem_used, mem_total = monitor.mem()
        disk_pct, disk_used, disk_total = monitor.disk()
        last_status = {"cpu": cpu, "mem": mem_pct, "disk": disk_pct}

        line = f"CPU {cpu:.0f}% | Minne {mem_pct:.0f}% | Disk {disk_pct:.0f}%"
        sys.stdout.write("\r" + line + " " * 10)
        sys.stdout.flush()

        # kolla larm
        hits = alarms.evaluate(cpu, mem_pct, disk_pct)
        alarms_triggered = []
        for a in hits:
            msg = f"LARM: {a['metric'].upper()} {a['direction']} {a['threshold']:.0f}%"
            alarms_triggered.append(msg)
            print(f"\n*** {msg} ***")

        # logga mätning + ev. larm
        session_log.append({
            "cpu": cpu,
            "mem": mem_pct,
            "disk": disk_pct,
            "alarms": alarms_triggered
        })

        time.sleep(1)
        i += 1

    monitoring_active = False
    print("\nAvslutar övervakning...")

def list_active():
    """Visar status om övervakning är igång."""
    if not monitoring_active:
        print("\nIngen övervakning är aktiv.")
    else:
        print("\n— Aktiv övervakning —")
        print(f"CPU: {last_status.get('cpu',0):.0f}%")
        print(f"Minne: {last_status.get('mem',0):.0f}%")
        print(f"Disk: {last_status.get('disk',0):.0f}%")
    press()

def create_alarm():
    """Meny för att skapa larm enligt instruktionerna."""
    print("\n=== Skapa larm ===")
    print("1. CPU (1–100)")
    print("2. Disk (1–100)")
    print("3. Memory (1–100)")
    choice = input("Välj: ").strip()

    if choice == "1":
        metric = "cpu"
    elif choice == "2":
        metric = "disk"
    elif choice == "3":
        metric = "memory"
    else:
        print("Fel val."); return

    t = input(f"Ställ in nivå för {metric.upper()} (1–100): ").strip()
    if not t.isdigit() or not (1 <= int(t) <= 100):
        print("Felaktig nivå."); return

    t = float(t)
    a = alarms.create(metric, t, ">=")
    print(f"Larm för {metric.upper()} satt till {t:.0f}%. (ID {a['id']})")
    press()

def show_alarms():
    """Visar alla larm, sorterade på typ."""
    L = sorted(alarms.list_all(), key=lambda a: a["metric"])
    if not L:
        print("\nInga larm."); press(); return

    print("\n— Larm —")
    for i,a in enumerate(L,1):
        print(f"{i}. {a['metric'].upper()} larm {a['threshold']:.0f}% (ID {a['id']})")
    press()

def edit_alarm():
    """Ändra eller ta bort ett larm."""
    L = alarms.list_all()
    if not L:
        print("Inga larm."); press(); return

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
    press()

def show_last_results():
    """Visar resultat från senaste övervakningen."""
    if not session_log:
        print("\nIngen övervakning har körts än.")
        press(); return

    print("\n=== Senaste övervakning ===")
    print(f"Totalt antal mätpunkter: {len(session_log)}")

    alarms_total = sum(len(x["alarms"]) for x in session_log)
    print(f"Totalt antal larm: {alarms_total}")

    # Skriv ut några exempel (senaste 5 raderna)
    print("\nSista mätpunkterna:")
    for row in session_log[-5:]:
        print(f"CPU {row['cpu']:.0f}%, Minne {row['mem']:.0f}%, Disk {row['disk']:.0f}%")
        for alarm in row["alarms"]:
            print(f"   -> {alarm}")
    press()

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
