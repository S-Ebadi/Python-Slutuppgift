# System Monitor - Main Application
import time
import json
import monitor 
import alarms 
import utils 
import logger

# Global state variables
monitoring_active = False
current_cpu = 0
current_ram = 0
current_disk = 0
session_data = []

def start_monitoring():
    global monitoring_active, current_cpu, current_ram, current_disk, session_data
    
    print("Starting system monitoring...")
    print("Monitoring will run 10 times, then stop automatically")
    
    # Set up monitoring
    monitoring_active = True
    session_data = []
    count = 0
    
    # Simple monitoring loop - runs 10 times
    while count < 10:
        count = count + 1
        
        # Get current values
        current_cpu = monitor.get_cpu()
        current_ram = monitor.get_ram()  
        current_disk = monitor.get_disk()
        
        # Show current status
        utils.pretty_print_status(current_cpu, current_ram, current_disk, count)
        
        # Check alarms
        alarm_messages = alarms.check_alarms(current_cpu, current_ram, current_disk)
        for message in alarm_messages:
            print("ALERT: " + message)
            logger.write_log(message)
        
        # Save session data
        timestamp = str(int(time.time()))
        entry = {"cpu": current_cpu, "ram": current_ram, "disk": current_disk, "time": timestamp}
        session_data.append(entry)
        
        # Wait before next reading
        if count < 10:
            print("Waiting 2 seconds...")
            time.sleep(2)
    
    # Stop monitoring
    print("\nMonitoring completed!")
    monitoring_active = False
    utils.save_session_data(session_data)
    logger.write_log("Monitoring stopped")

def show_status():
    if monitoring_active:
        status = "Monitoring active - CPU: " + str(current_cpu) + "% RAM: " + str(current_ram) + "% DISK: " + str(current_disk) + "%"
        print(status)
    else:
        print("Monitoring inactive")
    
    input("Press Enter to continue...")

def show_last_session():
    filename = utils.get_last_session_file()
    
    if filename:
        # Load session data
        with open(filename, "r") as f:
            data = json.load(f)
        
        # Show summary
        total_count = len(data)
        print("Total measurements: " + str(total_count) + " | Last 5 entries:")
        
        # Show last 5 entries
        last_entries = data[-5:]
        for entry in last_entries:
            line = entry["time"] + " - CPU: " + str(entry["cpu"]) + "% RAM: " + str(entry["ram"]) + "% DISK: " + str(entry["disk"]) + "%"
            print(line)
    else:
        print("No previous session found")
    
    input("Press Enter to continue...")

def simple_monitoring():
    print("Simple monitoring mode - showing 5 readings")
    
    # Show 5 simple readings
    for i in range(5):
        reading_number = i + 1
        print("Reading " + str(reading_number) + "/5:")
        
        cpu = monitor.get_cpu()
        ram = monitor.get_ram()
        disk = monitor.get_disk()
        
        utils.pretty_print_status(cpu, ram, disk)
        
        if reading_number < 5:
            print("Waiting 2 seconds...")
            time.sleep(2)
    
    print("Simple monitoring completed!")
    input("Press Enter to continue...")

def show_menu():
    print("\n=== SYSTEM MONITOR ===")
    print("1. Start monitoring")
    print("2. Show status")
    print("3. Create alarm")
    print("4. Show alarms")
    print("5. Edit alarms")
    print("6. Show last session")
    print("7. Simple mode")
    print("8. Exit")

def main():
    logger.write_log("Program started")
    
    try:
        # Main menu loop
        while True:
            show_menu()
            choice = input("Enter choice: ")
            
            # Handle menu choices
            if choice == "1":
                start_monitoring()
            elif choice == "2":
                show_status()
            elif choice == "3":
                alarms.create_new_alarm()
            elif choice == "4":
                alarms.show_all_alarms()
            elif choice == "5":
                alarms.edit_delete_alarms()
            elif choice == "6":
                show_last_session()
            elif choice == "7":
                simple_monitoring()
            elif choice == "8":
                print("Have a nice day, and remember that a hug each day keeps the worries away! 🤗")
                logger.write_log("Program ended")
                break
            else:
                print("You suck! Please try again and choose between 1-8.")
                
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
        logger.write_log("Program interrupted by Ctrl+C")
    except Exception as error:
        print("An error occurred:", str(error))
        logger.write_log("Program error: " + str(error))

if __name__ == "__main__":
    main()
