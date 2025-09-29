import time
from typing import Callable

from alarms import AlarmRegistry, AlarmType
from logger import log_event
from monitor import read_cpu_percent, read_memory, read_disk
from utils import ask_int_in_range, press_enter_to_continue, format_bytes, nonblocking_enter_loop


def print_header():
    print("\n=== Systemmonitor ===")


def print_main_options():
    print("\n1. Starta övervakning")
    print("2. Lista aktiv övervakning")
    print("3. Skapa larm")
    print("4. Visa larm")
    print("5. Starta övervakningsläge")
    print("6. Ta bort larm (VG)")
    print("7. Avsluta")


def main_menu(registry: AlarmRegistry, save_callback: Callable[[list], None]):
    monitoring_active = False

    while True:
        print_header()
        print_main_options()
        choice = input("\nVälj alternativ (1-7): ").strip()
        log_event(f"MENU_CHOICE={choice}")

        if choice == "1":
            # Starta övervakning (aktiverar flagga)
            monitoring_active = True
            print("\nÖvervakning startad (CPU, Minne, Disk).")
            log_event("MONITORING_ENABLED")
            press_enter_to_continue()

        elif choice == "2":
            # Lista status eller meddela att ej aktiv
            if not monitoring_active:
                print("\nIngen övervakning är aktiv.")
                log_event("STATUS_REQUEST_WHEN_MONITORING_DISABLED")
            else:
                cpu = read_cpu_percent()
                mem = read_memory()
                dsk = read_disk()
                print("\nAktiv övervakning:")
                print(f"CPU användning: {cpu:.0f}%")
                print(
                    f"Minnesanvändning: {mem['percent']:.0f}% ("
                    f"{format_bytes(mem['used'])} out of {format_bytes(mem['total'])} used)"
                )
                print(
                    f"Diskanvändning: {dsk['percent']:.0f}% ("
                    f"{format_bytes(dsk['used'])} out of {format_bytes(dsk['total'])} used)"
                )
                log_event(
                    f"STATUS_CPU={cpu:.0f}_MEM={mem['percent']:.0f}_DISK={dsk['percent']:.0f}"
                )
            press_enter_to_continue()

        elif choice == "3":
            # Skapa larm
            create_alarm_menu(registry, save_callback)

        elif choice == "4":
            # Visa larm
            list_alarms(registry)
            press_enter_to_continue()

        elif choice == "5":
            # Övervakningsläge – loopar och varnar, avbryt med valfri tangent (ENTER)
            if not monitoring_active:
                print("\nIngen övervakning är aktiv. Starta först via menyval 1.")
                log_event("MONITORING_MODE_REQUESTED_WHEN_DISABLED")
                press_enter_to_continue()
            else:
                print("\nÖvervakning är aktiv, tryck Enter för att återgå till menyn.")
                log_event("MONITORING_MODE_START")

                def tick_and_check():
                    cpu = read_cpu_percent()
                    mem = read_memory()
                    dsk = read_disk()
                    # Visa kort heartbeat
                    print(
                        f"Status: CPU {cpu:.0f}% | MEM {mem['percent']:.0f}% | DISK {dsk['percent']:.0f}%",
                        end="\r",
                        flush=True,
                    )
                    # Kolla larm – endast närmaste per typ får trigga
                    for atype, value in [
                        (AlarmType.CPU, cpu),
                        (AlarmType.MEMORY, mem["percent"]),
                        (AlarmType.DISK, dsk["percent"]),
                    ]:
                        trig = registry.closest_trigger(atype, value)
                        if trig is not None:
                            msg = (
                                f"***VARNING, LARM AKTIVERAT, {atype.name} ANVÄNDNING "
                                f"ÖVERSTIGER {int(trig.threshold)}%***"
                            )
                            print("\n" + msg)
                            log_event(f"ALARM_TRIGGERED_TYPE={atype.name}_THRESHOLD={int(trig.threshold)}_VALUE={int(value)}")

                # Kör loop med 1s intervall tills Enter trycks (icke-blockerande)
                nonblocking_enter_loop(tick_and_check, interval_sec=1.0)
                print("\nÅter till huvudmenyn.")
                log_event("MONITORING_MODE_EXIT")

        elif choice == "6":
            # Ta bort larm (VG)
            remove_alarm_menu(registry, save_callback)

        elif choice == "7":
            print("\nHejdå!")
            break
        else:
            print("\nOgiltigt val, försök igen.")
            log_event("MENU_CHOICE_INVALID")


def create_alarm_menu(registry: AlarmRegistry, save_callback: Callable[[list], None]):
    print("\n== Skapa larm ==")
    print("1. CPU användning")
    print("2. Minnesanvändning")
    print("3. Diskanvändning")
    print("4. Tillbaka")

    choice = input("Välj typ (1-4): ").strip()
    log_event(f"CREATE_ALARM_CHOICE={choice}")

    mapping = {"1": AlarmType.CPU, "2": AlarmType.MEMORY, "3": AlarmType.DISK}
    if choice == "4":
        return
    if choice not in mapping:
        print("Ogiltigt val.")
        return

    threshold = ask_int_in_range("Ställ in nivå för alarm mellan 1-100: ", 1, 100)
    atype = mapping[choice]
    registry.add_alarm(atype, threshold)
    save_callback(registry.as_dict_list())
    print(f"Larm för {atype.display()} satt till {threshold}%.")
    log_event(f"ALARM_CONFIGURED_TYPE={atype.name}_THRESHOLD={threshold}")


def list_alarms(registry: AlarmRegistry):
    print("\n== Aktiva larm ==")
    alarms = registry.get_sorted()
    if not alarms:
        print("Inga larm konfigurerade.")
        return

    # Funktionell stil: map + join
    lines = map(lambda a: f"{a.type.display()} larm {int(a.threshold)}%", alarms)
    for line in lines:
        print(line)


def remove_alarm_menu(registry: AlarmRegistry, save_callback: Callable[[list], None]):
    print("\n== Ta bort larm ==")
    alarms = registry.get_sorted()
    if not alarms:
        print("Inga larm att ta bort.")
        return

    for idx, a in enumerate(alarms, start=1):
        print(f"{idx}. {a.type.display()} larm {int(a.threshold)}%")
    choice = ask_int_in_range("Välj nummer att ta bort: ", 1, len(alarms))

    removed = registry.remove_by_sorted_index(choice - 1)
    if removed:
        save_callback(registry.as_dict_list())
        print(f"Tog bort {removed.type.display()} larm {int(removed.threshold)}%.")
        log_event(f"ALARM_REMOVED_TYPE={removed.type.name}_THRESHOLD={int(removed.threshold)}")
    else:
        print("Ogiltigt val.")
