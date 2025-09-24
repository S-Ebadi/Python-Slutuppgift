from typing import Optional
from alarms import AlarmType, AlarmManager
from monitor import read_status, human_status
import logging
import sys
import time

# Plattformskänslig "valfri tangent" för att avsluta övervakningsläge
def wait_for_any_key_nonblocking_prompt(prompt: str) -> None:
    print(prompt)
    try:
        if sys.platform.startswith("win"):
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    msvcrt.getch()
                    return
                time.sleep(0.1)
        else:
            # POSIX: använd select på stdin i "omedelbart" läge
            import termios, tty, select
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                while True:
                    dr, _, _ = select.select([sys.stdin], [], [], 0.1)
                    if dr:
                        sys.stdin.read(1)
                        return
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except Exception:
        # Fallback: ENTER
        input("Tryck ENTER för att återgå till menyn...")

def ask_int_between(prompt: str, low: int, high: int) -> Optional[int]:
    raw = input(prompt).strip()
    if not raw.isdigit():
        return None
    val = int(raw)
    if val < low or val > high:
        return None
    return val

class Menu:
    def __init__(self, alarm_manager: AlarmManager, logger: logging.Logger):
        self.alarm_manager = alarm_manager
        self.logger = logger
        self.monitoring_started = False  # "Starta övervakning" flagga

    def run(self):
        while True:
            self._print_main()
            choice = input("Välj [1-5] eller Q för att avsluta: ").strip().lower()
            self.logger.info(f"User_Input_{choice!r}")

            if choice in ("q", "quit", "exit"):
                self.logger.info("Program_avslutat")
                print("Avslutar. Tack.")
                break

            if choice == "1":
                self.start_monitoring()
            elif choice == "2":
                self.list_active_monitoring()
            elif choice == "3":
                self.configure_alarms_menu()
            elif choice == "4":
                self.show_alarms()
            elif choice == "5":
                self.start_monitoring_mode()
            else:
                print("Ogiltigt val. Försök igen.")

    # 1) Starta övervakning
    def start_monitoring(self):
        self.monitoring_started = True
        self.logger.info("Overvakning_startad")  # logikkrav
        print("Övervakning har startats (ingen automatisk start sker vid programstart).")

    # 2) Lista aktiv övervakning (utan att trigga larm!)
    def list_active_monitoring(self):
        if not self.monitoring_started:
            print("Ingen övervakning är aktiv.")
            input("Tryck ENTER för att återgå till huvudmeny...")
            return

        status = read_status()
        print(human_status(status))
        input("Tryck ENTER för att återgå till huvudmeny...")

    # 3) Skapa larm (submenu)
    def configure_alarms_menu(self):
        while True:
            print("\n--- Konfigurera larm ---")
            print("1) CPU användning")
            print("2) Minnesanvändning")
            print("3) Diskanvändning")
            print("4) Ta bort larm")
            print("5) Tillbaka till huvudmeny")
            sub = input("Välj [1-5]: ").strip()
            self.logger.info(f"User_Input_Sub_{sub!r}")

            if sub == "5":
                return
            elif sub == "4":
                self.remove_alarm_flow()
                continue

            alarm_type_map = {"1": AlarmType.CPU, "2": AlarmType.MEM, "3": AlarmType.DISK}
            if sub not in alarm_type_map:
                print("Ogiltigt val.")
                continue

            level = ask_int_between("Ställ in nivå för larm mellan 1-100: ", 1, 100)
            if level is None:
                print("Fel: Ange ett heltal 1-100.")
                continue

            at = alarm_type_map[sub]
            self.alarm_manager.add_alarm(at, level)
            self.logger.info(f"{at.value}_Användningslarm_Konfigurerat_{level}_Procent")
            print(f"Larm för {at.display_name} satt till {level}%.")

    def remove_alarm_flow(self):
        alarms = self.alarm_manager.list_sorted()
        if not alarms:
            print("Inga larm att ta bort.")
            return

        print("\nVälj ett konfigurerat larm att ta bort:")
        for idx, a in enumerate(alarms, start=1):
            print(f"{idx}) {a.type.display_name} {a.threshold}%")

        choice = ask_int_between("Ange siffra: ", 1, len(alarms))
        if choice is None:
            print("Fel: Ogiltigt val.")
            return

        chosen = alarms[choice - 1]
        self.alarm_manager.remove_alarm(chosen)
        self.logger.info(f"{chosen.type.value}_Larm_borttaget_{chosen.threshold}_Procent")
        print("Larm borttaget.")

    # 4) Visa larm (sorterade)
    def show_alarms(self):
        alarms = self.alarm_manager.list_sorted()
        if not alarms:
            print("Inga larm är konfigurerade.")
        else:
            for a in alarms:
                print(f"{a.type.display_name} {a.threshold}%")
        input("Tryck ENTER för att gå tillbaka till huvudmeny...")

    # 5) Starta övervakningsläge (triggar larm i loop tills tangent)
    def start_monitoring_mode(self):
        if not self.monitoring_started:
            print("Ingen övervakning är aktiv. Starta den först (val 1).")
            return

        self.logger.info("Overvakningslage_startat")
        print("\nÖvervakning är aktiv, tryck på valfri tangent för att återgå till menyn.\n")

        # loop tills tangent
        while True:
            status = read_status()
            # Meddelande om aktiv loop (diskret)
            print(".", end="", flush=True)

            # Kontrollera larm (endast här – EJ i menyinteraktion)
            trigs = self.alarm_manager.check_triggers(
                cpu=status["cpu_percent"],
                mem=status["mem_percent"],
                disk=status["disk_percent"],
            )
            for t in trigs:
                msg = f"***VARNING, LARM AKTIVERAT, {t}***"
                print("\n" + msg)
                # Logg enligt krav, t.ex.: CPU_Användningslarm_aktiverat_80_Procent
                self.logger.info(t.replace(" ", "_"))

            # Känn av tangent utan att blockera
            try:
                # En snabb "poll" + bryt om tangent
                import threading
                flag = {"stop": False}
                th = threading.Thread(target=wait_for_any_key_nonblocking_prompt, args=("",))
                th.daemon = True
                th.start()
                time.sleep(0.9)  # ca 1 Hz uppdatering
                if th.is_alive():
                    # ingen tangent tryckt – fortsätt
                    continue
                else:
                    break
            except Exception:
                # Fallback: fast frekvens + manual break via Ctrl+C
                time.sleep(1.0)

        print("\nÅter till huvudmeny.")
        self.logger.info("Overvakningslage_stoppat")
