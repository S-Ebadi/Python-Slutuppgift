from menu import main_menu
from alarms import AlarmRegistry
from storage import load_alarms, save_alarms
from logger import init_logger, log_event


def bootstrap() -> AlarmRegistry:
    # Init logging (ny fil per körning)
    init_logger()
    log_event("PROGRAM_START")

    # Ladda tidigare larm från disk
    print("loading previously configured alarms...")
    log_event("LOAD_PREVIOUS_ALARMS_START")
    loaded = load_alarms()
    registry = AlarmRegistry(loaded)
    log_event(f"LOAD_PREVIOUS_ALARMS_DONE_COUNT={len(loaded)}")
    return registry


def main():
    registry = bootstrap()
    try:
        main_menu(registry, save_callback=lambda alarms: save_alarms(alarms))
    except KeyboardInterrupt:
        print("\nAvslutar...")
        log_event("PROGRAM_KEYBOARD_INTERRUPT")
    finally:
        log_event("PROGRAM_EXIT")


if __name__ == "__main__":
    main()
